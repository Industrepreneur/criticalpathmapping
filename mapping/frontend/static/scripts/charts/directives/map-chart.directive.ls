'use strict'

/**
 * Generate a MAP chart with supplied data
 *
 * @memberof mapping.charts.directives.mapChart
 * @todo Move percentage calculations into SheetService
 */
angular.module 'mapping.charts.directives' .directive 'mapChart', ->
    restrict: 'E'
    scope:
        sheet: '='
    template: template-fn
    controller: controller-fn


function template-fn (element, attrs)
    "<div class=\"mapchart-container\"><canvas class=\"map-canvas\"></canvas></div>"


controller-fn.$inject = <[ $scope $filter $document $window $element $attrs $log oCanvas ]>
!function controller-fn ($scope, $filter, $document, $window, $element, $attrs, $log, oCanvas)
    var blocks
        canvas
        chart-data
        chart-elem
        center-x
        center-y
        indicator-proto
        slice-proto


    date-format     = 'YYYY-MM-DD HH:mm'
    min-slice-width = 3
    chart-type      = $attrs.chart-type or 'detailView'
    overlay-type    = $attrs.overlay-type or 'visible'
    sheet           = $scope.sheet

    init-chart!
    draw-chart!

    /*angular.element $window .bind \resize, _.debounce draw-chart, 500*/

    /*Trigger redraw on sheet update*/
    $scope.$on \sheet.updated, (event, new-sheet) !->
        return unless new-sheet[chart-type]
        sheet      := new-sheet
        chart-data := new-sheet[chart-type]
        blocks     := chart-data.blocks
        draw-chart!


    /**
     * @private
     */
    !function init-chart
        # @todo render error message if invalid chart
        chart-data := sheet[chart-type]
        chart-elem   := $element.find('canvas')[0]
        canvas     := oCanvas.create do
            canvas           : chart-elem
            clear-each-frame : true
            draw-each-frame  : false

        size-canvas!

        slice-proto := canvas.display.rectangle do
            height : canvas.height
            origin : x: 'left', y: 'top'

        indicator-proto := canvas.display.rectangle do
            origin : x : 'center', y : 'top'
            height : 5


    /**
     * @private
     */
    !function draw-chart
        return unless sheet[chart-type]
        blocks := chart-data.blocks
        slices  = []
        clear-canvas!
        size-canvas!
        size-blocks!

        for block in blocks
            block <<<
                style: switch chart-type
                       | 'detailView'  => $filter('operationTypeStyle') block.type
                       | 'summaryView' => $filter('valueTypeStyle') block.value-type
                       | 'shopView'    => $filter('operationTypeStyle') block.type

        last-end = 0
        for block in blocks
            block-start = block.start.format date-format
            block-end   = block.end.format date-format
            block-hours = $filter('number') (moment.duration block.duration .as-hours!), 2
            label       = switch chart-type
                          | 'detailView'  => "#{block-hours}h (#{block-start} to #{block-end}): #{block.type-name} - #{block.value-type} - #{block.percent}%"
                          | 'summaryView' => "#{block-hours}h: #{block.value-type} - #{block.percent}%"
                          | 'shopView'    => "#{block-hours}h: #{block.type-name} - #{block.value-type} - #{block.percent}%"
                          | otherwise     => ''

            slice = slice-proto.clone do
                fill   : block.style.fill ?: '#333'
                x      : last-end
                y      : 0
                height : canvas.height
                width  : block.width
                label  : label

            /*Create striped overlay if required*/
            if block.style.is_striped
                slice.add-child slice-proto.clone do
                    pointer-events : false
                    fill           : 'image(/static/images/diagonal_stripes_bg2.png, repeat)'
                    x              : 0
                    y              : 0
                    height         : slice.height
                    width          : slice.width

            slice
            .bind 'mouseenter touchenter', ->
                label.text = @label

                # Disable animations temporarily
                # $log.log "mouseenter", this
                with slice-ind
                    ..x     = @width / 2 + @abs_x - center-x
                    ..width = @width
                canvas.redraw!

                # slice-ind.stop!animate do
                #   * width: @width
                #     x: @width / 2 + @abs_x - center-x
                #   * duration: 0

            slices.push slice
            canvas.add-child slice
            last-end = last-end + slice.width

        label = canvas.display.text do
            y: -5
            origin : x : 'center', y : 'bottom'
            align  : 'center'
            font   : 'normal 14px Roboto'
            fill   : 'rgba(0, 0, 0, 0.9)'

        sbar-fill   = 'rgba(255, 255, 255, 0.65)'
        sbar-height = label.height + 10

        slice-ind = indicator-proto.clone do
            y    : -sbar-height - 5
            fill : sbar-fill

        sbar-y = canvas.height + sbar-height
        sbar = canvas.display.rectangle do
            fill   : sbar-fill
            x      : center-x
            y      : sbar-y
            origin : x: 'center', y: 'bottom'
            height : sbar-height
            width  : canvas.width

        canvas
        .bind 'mouseenter touchenter', ->
            # Disable animations temporarily
            sbar.y = canvas.height
            canvas.redraw!

            # sbar.finish!animate do
            #   * y        : canvas.height
            #   * duration : 250
            #     easing   : \ease-in-quartic

        .bind 'mouseleave touchleave', ->
            # Disable animations temporarily
            label.text = ''
            sbar.y     = sbar-y
            with slice-ind
                ..x     = canvas.x
                ..width = 0
            canvas.redraw!

            # slice-ind.stop!animate do
            #   * width    : 0
            #     x        : canvas.x
            #   * duration : 250

            # sbar.animate do
            #   * y        : sbar-y
            #   * duration : \short
            #     easing   : \ease-out-quartic
            #     callback : -> label.text = ''

        sbar.add-child slice-ind
        sbar.add-child label
        canvas.add-child sbar unless overlay-type is 'hidden'


    /**
     * @private
     */
    !function clear-canvas then canvas.clear!


    /**
     * Resize canvas to fill entire parent container
     *
     * @private
     */
    !function size-canvas
        canvas.width   = chart-elem.client-width
        canvas.height  = chart-elem.client-height - 5
        center-x      := canvas.width / 2
        center-y      := canvas.height / 2


    /**
     * Calculate the width of each block based on the total canvas size
     *
     * @private
     */
    !function size-blocks
        duration = chart-data.duration or 1

        /*Make sure slices have a minimum width*/
        reserved = blocks.length * min-slice-width
        ratio    = (canvas.width - reserved) / duration

        for block in blocks
            block.width   = Math.floor((block.duration ?: 0) * ratio) + min-slice-width
            block.percent = $filter('number') (block.duration / duration * 100), 2

        remainder = canvas.width - _.sum(blocks, 'width')
        sorted    = _.sort-by blocks, 'duration'

        /*Spread remaining width across blocks from smallest to largest,
          skipping blocks that are only the minimum slice width.*/
        while remainder > 0
            for i til sorted.length when sorted[i].width > min-slice-width
                continue if remainder is 0
                sorted[i].width += 1
                remainder       -= 1
