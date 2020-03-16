'use strict'

datefmt = 'MM-DD HH:mm'

angular.module 'mapping.sheets.services'
    .factory 'SheetsService', sheets-service

sheets-service.$inject = <[ $filter $log Restangular DAYS OPERATION_TYPES operationTypeFilter WorkPeriodsService ]>
function sheets-service ($filter, $log, Restangular, DAYS, OPERATION_TYPES, operationTypeFilter, WorkPeriods)
    var _periods, _periods-by-id

    return new class Sheets
        /**
         * Constructor for SheetsService
         *
         * @constructor
         * @memberof mapping.sheets.services.SheetsService
         */
        -> @sheets = void


        /**
         * Create a new Sheet with provided parameters
         *
         * @memberof mapping.sheets.services.SheetsService
         * @param {Object} newSheet - JSON object containing new Sheet data
         * @returns {Promise}
         */
        create: (new-sheet) ->
            # $log.debug 'new-sheet', new-sheet
            Restangular.all \sheets
                .post new-sheet
                .then (sheet) ~> @sheets.push sheet; sheet


        /**
         * Retrieve all Sheets for the specified Part
         *
         * @memberof mapping.sheets.services.SheetsService
         * @param {number} partId - The id of the part to filter by
         * @returns {Promise}
         */
        for-part: (part-id) ->
            Restangular.one \parts, part-id
                .all \sheets
                .get-list!
                .then (sheets) ~>
                    _.each sheets, (sheet) -> _update-calculations sheet
                    @sheets = sheets


        /**
         * Get one Sheet by id
         *
         * @memberof mapping.sheets.services.SheetsService
         * @param {number} id - The sheet id to retrive
         * @returns {Promise}
         * @todo update @sheets object
         */
        one: (id) ->
            Restangular.one \sheets, id
                .get!
                .then (sheet) -> _update-calculations sheet


        /**
         * Delete a Sheet
         *
         * @memberof mapping.sheets.services.SheetsService
         * @param {Object} sheet - the sheet to be removed
         * @returns {Promise}
         */
        remove: (sheet) ->
            sheets = @sheets
            id     = _.find-key sheets, id: sheet
            sheets[id].remove!finally -> sheets.splice id, 1


        /**
         * Save or update a Sheet
         *
         * @memberof mapping.sheets.services.SheetsService
         * @param {Object} sheet - The sheet to be updated
         * @returns {Promise}
         */
        save: (sheet) ->
            sheet = _update-calculations sheet
            sheet.save!then (sheet) -> sheet


    /**
     * Calculate Sheet/Operation durations along with MCT Totals
     *
     * @private
     * @param {Object} sheet - the Sheet instance to update
     */
    function _update-calculations (sheet)

        /*Make sure WorkPeriods have been resolved first*/
        WorkPeriods.all!then (periods) ->
            _periods       := periods
            _periods-by-id := _.index-by _periods, \id

            with sheet
                _calc-operations-durations ..
                _calc-sheet-durations ..
                _calc-mct-totals ..
                _calc-duration-totals ..
                _calc-operation-shifts ..

                /*Inject MAP and PIE chart calculations*/
                if sheet.operations.length > 0
                    ..detail-view    = _detail-view-values ..
                    ..summary-view   = _summary-view-values ..
                    ..shop-view      = _shop-view-values ..
                    ..operation-type = _operation-type-values ..
                    ..value-type     = _value-type-values ..
                    # _debug ..

        return sheet


    /**
    * Calculate Operation durations
    *
    * @private
    * @param {Object} sheet - the Sheet instance to update
    */
    !function _calc-operations-durations (sheet)
        prev-op    = void
        operations = sheet.operations
        release    = moment sheet.release_date

        /*Iterate through each operation and add calculations*/
        for op in operations
            /*Skip incomplete operations that don't have start or end values*/
            return unless op.date_started? and op.date_completed?

            /*Calculate Ops durations*/
            start    = moment op.date_started
            end      = moment op.date_completed
            duration = end.diff start

            /**
             * Calculate "actual values", where first operation should start on
             * release_date, and subsequent operations should start at previous
             * operation end.
             */
            start-actual    = | prev-op?  => prev-op.end
                              | release?  => release
                              | otherwise => start
            duration-actual = end.diff start-actual

            /*Push calculations onto operation*/
            op <<<
                start                : start
                start-actual         : start-actual
                end                  : end
                duration             : duration
                duration-actual      : duration-actual
                duration-days        : _as-days duration
                duration-days-actual : _as-days duration-actual
            prev-op := op


    /*
     * Calculate Sheet durations
     *
     * @private
     * @param {Object} sheet - the sheet instance to update
     */
    !function _calc-sheet-durations (sheet)
        dates      = []
        operations = sheet.operations
        release    = moment sheet.release_date

        for op in operations then dates.push op.start, op.end

        start           = moment.min dates
        start-actual    = release
        end             = moment.max dates
        duration        = end.diff start

        # NOTE: When we have no operations yet created the base calculation needs to be set to 0
        #       in order to prevent incorrect calculation of the Sheet duration.
        duration-actual = if operations.length > 0 then end.diff(start-actual) else 0

        with sheet
            ..start                = start
            ..start-actual         = start-actual
            ..end                  = end
            ..duration             = duration
            ..duration-actual      = duration-actual
            ..duration-days        = _as-days duration
            ..duration-days-actual = _as-days duration-actual


    /**
     * Calculate MCT totals
     *
     * @private
     * @param {Object} sheet - the Sheet instance to update
     */
    !function _calc-mct-totals (sheet)
        duration-days = moment.duration!
            ..add (sheet.logistics_estimate or 0), \days
            ..add (sheet.raw_materials_estimate or 0), \days
            ..add (sheet.office_estimate or 0), \days
            ..add (sheet.finished_goods_estimate or 0), \days
        duration = duration-days.as-milliseconds!

        with sheet
            ..mct-duration      = duration
            ..mct-duration-days = _as-days duration


    /**
     * Calculate duration totals
     *
     * @private
     * @param {Object} sheet - the Sheet instance to calculate
     */
    function _calc-duration-totals (sheet)
        total-duration        = sheet.mct-duration + sheet.duration
        total-duration-actual = sheet.mct-duration + sheet.duration-actual
        ops-duration          = _(sheet.operations).reduce (m, x) -> (m + x.duration), 0
        ops-duration-actual   = _(sheet.operations).reduce (m, x) -> (m + x.duration-actual), 0

        with sheet
            ..total-duration             = total-duration
            ..total-duration-days        = _as-days total-duration
            ..total-duration-actual      = total-duration-actual
            ..total-duration-days-actual = _as-days total-duration-actual
            ..ops-duration               = ops-duration
            ..ops-duration-days          = _as-days ops-duration
            ..ops-duration-actual        = ops-duration-actual
            ..ops-duration-days-actual   = _as-days ops-duration-actual


    /**
    * Calculate values for Operation Type PIE chart
    *
    * @private
    * @param {Object} sheet
    */
    function _operation-type-values (sheet)
        view    = sheet.detail-view
        grouped = _.group-by view.blocks, 'type'

        _.each grouped, (g) -> g.duration = _.sum g, 'duration'
        total = _.sum grouped, 'duration'

        blocks = []
        _.each grouped, (g) ->
            percent = g.duration / total * 100
            type    = g.0.type
            blocks.push do
                type            : type
                duration        : g.duration
                duration-days   : _as-days g.duration
                percent         : percent
                percent-display : ($filter('number') percent, 2) + '%'
                type-name       : $filter('operationType') type
                value-type      : $filter('valueType') type

        duration = _.sum blocks, 'duration'

        return
            blocks   : blocks
            duration : duration


    /**
     * Calculate values for Value Type PIE chart
     *
     * @private
     * @param {Object} sheet
     */
    function _value-type-values (sheet)
        view    = sheet.summary-view
        grouped = _.group-by view.blocks, 'valueType'

        _.each grouped, (g) -> g.duration = _.sum g, 'duration'
        total = _.sum grouped, 'duration'

        blocks = []
        _.each grouped, (g, key) ->
            percent = g.duration / total * 100
            blocks.push do
                duration        : g.duration
                duration-days   : _as-days g.duration
                percent         : percent
                percent-display : ($filter('number') percent, 2) + \%
                type-name       : key
                value-type      : key

        /*Reverse block order so they line up with Operation Type values*/
        blocks.reverse!

        /*Inject blocks indexed by Value Type onto sheet*/
        _.each blocks, (block) -> sheet[block.value-type] = block

        duration = _.sum blocks, 'duration'

        return
            blocks   : blocks
            duration : duration


    /**
     * Calculate Operations time mapping relative to WorkPeriods
     *
     * @private
     */
    function _calc-operation-shifts (sheet)
        for op in sheet.operations
            op.shifts = _shifts-for-op op, _periods-by-id


    /**
     * Calculate the shifts which overlap the selected Operations
     *
     * @private
     * @param {Object} op - The Operation to map
     * @param {Object} periods - WorkPeriods for the current company
     */
    function _shifts-for-op (op, periods)
        return [] if op.operation_type is OPERATION_TYPES.OUTSIDE_PROCESSING

        op-start     = op.start-actual
        op-day-start = moment op-start .start-of \day
        op-end       = moment op.end
        op-start-dow = op-start.day!
        op-start-doy = op-start.day-of-year!
        op-end-doy   = op-end.day-of-year!
        op-range     = moment.range op-start, op-end

        # Determine how many days the operation spans
        # @todo This is a naive approach, and may not work with operations
        # that cross year boundary
        span-days = if op-end-doy >= op-start-doy
                    then op-end-doy - op-start-doy + 1
                    else 0

        shifts = []
        dow = op-start-dow
        for i in [0 til span-days]
            # get shifts for this day
            for shift in periods[op.work_period].shifts-by-days[dow]
                start       = moment.duration shift.start
                end         = moment.duration shift.end
                shift-start = moment op-start .add i, \days .start-of \day .add start
                shift-end   = moment op-start .add i, \days .start-of \day .add end
                range       = moment.range shift-start, shift-end
                shifts.push range if range.overlaps op-range

            # Day of Week must always be 0 (Sunday) through 6 (Saturday)
            dow = if dow is DAYS.SATURDAY then DAYS.SUNDAY else dow + 1

        return shifts


    /**
     * Return a single time block
     *
     * @param {int} type - The block type ID
     * @param {Object} op - The Operation to map
     * @param {moment} start - The start time
     * @param {moment} end - The end time
     * @returns {Object} - The generated block
     */
    function _create-block ({type, op, start, end, dbg = ''})
        return false if start >= end
        return
            dbg        : dbg
            op         : op
            start      : start
            end        : end
            duration   : end.diff start
            type       : type
            type-name  : $filter('operationType') type
            value-type : $filter('valueType') type


    /**
     * Generate pre-Operation blocks
     *
     * @param {Objects} shifts - Collection of shifts that overlap range
     * @param {moment} start - Starting time
     * @param {moment} end - Finish time
     * @returns {array} blocks to add to calculations
     */
    function _map-pre-operation (op, start, end)
        blocks   = []
        shifts   = op.shifts or []
        last-end = start
        range    = moment.range start, end
        proto    = op: op

        for shift in shifts when range.contains shift.start or range.contains shift.end
            mid-shift = if last-end >= shift.start then true else false

            /*Add off-hours block*/
            block = _create-block do
                dbg   : "pr-off-hours, MS: #{mid-shift}"
                op    : op
                start : last-end
                end   : if mid-shift then shift.end else shift.start
                type  : if mid-shift
                        then OPERATION_TYPES.WAIT_FOR_RESOURCE
                        else OPERATION_TYPES.OFF_HOURS
            if block then blocks.push block; last-end := block.end

            /*Add on-shift block*/
            block = _create-block do
                dbg   : \pr-on-shift
                op    : op
                start : last-end
                end   : if end < shift.end then end else shift.end
                type  : OPERATION_TYPES.WAIT_FOR_RESOURCE
            if block then blocks.push block; last-end := block.end

        /*Add remainder block*/
        if last-end < end
            blocks.push _create-block do
                dbg   : \pr-remainder
                op    : op
                start : last-end
                end   : end
                type  : if last-end <= shift?.end
                        then OPERATION_TYPES.WAIT_FOR_RESOURCE
                        else OPERATION_TYPES.OFF_HOURS

        return blocks


    /**
     * Map OUTSIDE PROCESSING type Operations
     *
     * @param {Object} op - The Operation to map
     * @param {Object} lastOp - The previous Operation
     * @returns {array}
     */
    function _map-offsite-operation (op, last-op)
        blocks = []

        block = _create-block do
            dbg   : \outside-processing
            op    : op
            start : last-op? and last-op.end or op.start
            end   : op.end
            type  : op.operation_type
        if block then blocks.push block

        return blocks


    /**
     * Map PIECE type Operations
     *
     * @param {Object} op - The Operation to map
     * @param {Object} lastOp - The previous Operation
     * @returns {array}
     */
    function _map-piece-operation (op, last-op)
        blocks   = []
        shifts   = op.shifts or []
        type     = op.operation_type or null
        start    = op.start
        end      = op.end
        /*duration = op.end - op.start*/
        last-end = op.start

        /*Calculate first piece duration only within shifts*/
        on-shift-duration = 0
        for shift in shifts when start <= shift.end
            /*$log.debug "[#{op.id}] shift", shift*/
            on-shift-start     = _.max [start, shift.start]
            on-shift-end       = _.min [end, shift.end]
            on-shift-duration += on-shift-end - on-shift-start

        first-piece-duration = on-shift-duration / (op.quantity_in ?: 1)

        /*Calculate first-piece end*/
        if op.quantity_in is 1 or shifts.length is 0
            first-piece-end = end

        else
            /*Piece quantity is greater than 1*/
            countdown = first-piece-duration
            for shift in shifts when start <= shift.end
                shift-start    = _.max [start, shift.start]
                shift-end      = _.min [end, shift.end]
                shift-duration = shift-end - shift-start

                if countdown <= shift-duration
                    first-piece-end = moment shift-start .add countdown
                    break

                countdown -= shift-duration

            #$log.debug "
            #    [#{op.id}]
            #    , dur: #{moment.duration op.duration .as-hours!}
            #    , osd: #{moment.duration on-shift-duration .as-hours!}
            #    , str: #{start.format(datefmt)}
            #    , fpd: #{moment.duration first-piece-duration .as-hours!}
            #    , fpe: #{first-piece-end.format(datefmt)}
            #    , end: #{end.format(datefmt)}
            #    "

        for shift in shifts when start <= shift.end
            if shift.start > last-end
                /*Create pre-shift off-hours block*/
                block = _create-block do
                    dbg   : \pc-off-hours
                    op    : op
                    start : last-end
                    end   : shift.start
                    type  : OPERATION_TYPES.OFF_HOURS
                if block then blocks.push block; last-end := block.end

            if first-piece-end >= shift.end
                /*Create full-shift first piece block*/
                block = _create-block do
                    dbg   : \pc-full-first-piece
                    op    : op
                    start : last-end
                    end   : shift.end
                    type  : type
                if block then blocks.push block; last-end := block.end
                continue

            /*Create partial-shift first piece block*/
            block = _create-block do
                dbg   : \pc-first-piece
                op    : op
                start : last-end
                end   : first-piece-end
                type  : type
            if block then blocks.push block; last-end := block.end
            /*first-piece = false*/

            /*Create shift remainder block*/
            block-end = if op.end < shift.end then op.end else shift.end
            block = _create-block do
                dbg   : \pc-processing-piece
                op    : op
                start : last-end
                end   : block-end
                type  : OPERATION_TYPES.WAIT_FOR_LOT
            if block then blocks.push block; last-end := block.end

        /*Add remainder block*/
        if last-end < end
            blocks.push _create-block do
                dbg   : \pc-remainder
                op    : op
                start : last-end
                end   : end
                type  : OPERATION_TYPES.OFF_HOURS

        return blocks


    /**
     * Map BATCH and standard Operations
     *
     * @param {Object} op - The Operation to map
     * @param {Object} lastOp - The previous Operation
     * @returns {array}
     */
    function _map-standard-operation (op)
        blocks   = []
        shifts   = op.shifts or []
        type     = op.operation_type or null
        start    = op.start
        end      = op.end
        last-end = op.start

        for shift in shifts when start <= shift.end
            /*Create pre-shift off-hours block*/
            if shift.start > last-end
                block = _create-block do
                    dbg   : \off-hours
                    op    : op
                    start : last-end
                    end   : shift.start
                    type  : OPERATION_TYPES.OFF_HOURS
                if block then blocks.push block; last-end := block.end

            /*Create on-hours block*/
            block = _create-block do
                dbg   : \op-on-hours
                op    : op
                start : last-end
                end   : if op.end < shift.end then op.end else shift.end
                type  : type
            if block then blocks.push block; last-end := block.end

        /*Add remainder block*/
        if last-end < end
            blocks.push _create-block do
                dbg   : \op-remainder
                op    : op
                start : last-end
                end   : end
                type  : OPERATION_TYPES.OFF_HOURS

        return blocks



    function _map-operations (sheet, op, last-op)
        blocks  = []
        shifts  = op.shifts or []
        release = sheet.release_date? and moment sheet.release_date or op.end
        type    = op.operation_type

        /*First generate pre-Operation blocks*/
        pre-op-start  = last-op? and last-op.end or release
        pre-op-blocks = _map-pre-operation op, pre-op-start, op.start
        for block in pre-op-blocks then blocks.push block

        /*Next map Operation blocks*/
        op-blocks = switch type
            | OPERATION_TYPES.OUTSIDE_PROCESSING => _map-offsite-operation op, last-op
            | OPERATION_TYPES.PROCESSING_PIECE   => _map-piece-operation op, last-op
            | OPERATION_TYPES.INSPECTION_PIECE   => _map-piece-operation op, last-op
            | otherwise                          => _map-standard-operation op
        for block in op-blocks then blocks.push block

        return blocks


    /**
     * Create breakdown for detailView MAP
     *
     * @private
     * @param {Object} sheet
     * @returns {Object}
     */
    function _detail-view-values (sheet)
        operations = ^^sheet.operations or []
        blocks     = []
        last-op    = void
        curr-op    = void

        /*Walk through each Operation*/
        for op in operations
            last-op := curr-op
            curr-op := op
            for block in _map-operations(sheet, op, last-op) then blocks.push block

        /*calculate duration*/
        duration = _.sum blocks, 'duration'
        start    = blocks.0? and blocks.0.start or moment!
        end      = blocks[*-1].end or start

        return
            blocks   : blocks
            start    : start
            end      : end
            duration : duration


    /**
     * Create breakdown for summaryView MAP
     *
     * Summary View values consist of grouped values by Value Type.
     * Values are calculated from the Detail View breakdown by grouping blocks
     * of the same Value Type which connect with each other, regardless of the
     * operation they belong to.
     *
     * @private
     * @param {Object} sheet
     * @returns {Object}
     */
    function _summary-view-values (sheet)
        detail-blocks = sheet.detail-view.blocks
        total-blocks  = detail-blocks.length
        blocks        = []
        last-block    = void
        for b, i in detail-blocks
            /*Merging previous block with current or creating a new one?*/
            merge = last-block? and b.value-type is last-block.value-type

            if merge then last-block <<<
                end      : b.end
                duration : b.end.diff last-block.start

            else then block = _create-block do
                op    : b.op
                start : b.start
                end   : b.end
                type  : b.type

            last-block := block
            blocks.push block if not merge or i >= total-blocks

        /*calculate total duration*/
        duration = _.sum blocks, 'duration'
        start    = blocks.0? and blocks.0.start or moment!
        end      = blocks[*-1].end or start

        return
            blocks   : blocks
            start    : start
            end      : end
            duration : duration


    /**
     * Create breakdown for shopView MAP
     *
     * @private
     * @param {Object} sheet
     * @returns {Object}
     */
    function _shop-view-values (sheet)
        detail-blocks = sheet.detail-view.blocks
        total-blocks  = detail-blocks.length
        blocks        = []
        last-block    = void
        for b, i in detail-blocks
            /*Skip OFF_HOURS blocks*/
            continue if b.type is OPERATION_TYPES.OFF_HOURS

            /*Merging previous block with current or creating a new one?*/
            merge = last-block? and b.type is last-block.type

            if merge then last-block <<<
                end      : b.end
                duration : b.end.diff last-block.start

            else then block = _create-block do
                op    : b.op
                start : b.start
                end   : b.end
                type  : b.type

            last-block := block
            blocks.push block if not merge or i >= total-blocks

        /*calculate total duration*/
        duration = _.sum blocks, 'duration'
        start    = blocks.0? and blocks.0.start or moment!
        end      = blocks[*-1].end or start

        return
            blocks   : blocks
            start    : start
            end      : end
            duration : duration


    /**
     * Convert duration in milliseconds to dur-days
     *
     * @param {number} time - Time value in milliseconds
     * @returns {number}
     */
    function _as-days (time)
        Math.ceil(moment.duration(time).as-days! * 100) / 100


    /**
     * Output debugging information to developer console
     */
    !function _debug (sheet)
        _debug-operations-shifts sheet
        _debug-detail-view-values sheet
        _debug-summary-view-values sheet
        _debug-shop-view-values sheet


    !function _debug-operations-shifts (sheet)
        console.group-collapsed 'Operations Shifts'
        for let op, i in sheet.operations
            console.group-collapsed "#{op.start.format(datefmt)} - #{op.end.format(datefmt)} :#{$filter(\operationType) op.operation_type}"
            # for shift in op.shifts
            #     $log.debug "#{shift.start.format(datefmt)} - #{shift.end.format(datefmt)}"
            console.group-end!
        console.group-end!


    !function _debug-detail-view-values (sheet)
        blocks = sheet.detail-view.blocks
        display = []
        for block in blocks
            display.push do
                op-id : block.op? and block.op.id or null
                start : block.start.format(datefmt)
                end   : block.end.format(datefmt)
                hours : (moment.range block.start, block.end .diff 'minutes') / 60
                type  : block.type-name
                logic : block.dbg
        console.group-collapsed "Detail View (#{blocks.length})"
        console.table display
        console.group-end!


    !function _debug-summary-view-values (sheet)
        blocks = sheet.summary-view.blocks
        display = []
        for block in blocks
            display.push do
                op-id : block.op? and block.op.id or null
                start : block.start.format(datefmt)
                end   : block.end.format(datefmt)
                hours : (moment.range block.start, block.end .diff 'minutes') / 60
                type  : block.type-name
        console.group-collapsed "Summary View (#{blocks.length})"
        console.table display
        console.group-end!


    !function _debug-shop-view-values (sheet)
        blocks = sheet.shop-view.blocks
        display = []
        for block in blocks
            display.push do
                op-id : block.op? and block.op.id or null
                start : block.start.format(datefmt)
                end   : block.end.format(datefmt)
                hours : (moment.range block.start, block.end .diff 'minutes') / 60
                type  : block.type-name
        console.group-collapsed "Shop View (#{blocks.length})"
        console.table display
        console.group-end!
