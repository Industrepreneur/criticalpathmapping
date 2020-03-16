'use strict'

/**
 * Generate a PIE chart with supplied data
 * @memberof mapping.charts.directives.pieChart
 */
angular.module 'mapping.charts.directives' .directive 'pieChart', ->
    restrict: 'E'
    scope:
        sheet: '='
    template: template-fn
    controller: controller-fn


function template-fn (element, attrs)
    "<div class=\"piechart-container\"><canvas class=\"pie-canvas\"></canvas></div>"


controller-fn.$inject = <[ $scope $filter $document $window $element $attrs $log oCanvas ]>
!function controller-fn ($scope, $filter, $document, $window, $element, $attrs, $log, oCanvas)
    var blocks
        canvas
        chart-data
        chart-elem
        center-x
        center-y
        radius
        slice-proto

    min-slice-angle = 3
    chart-type      = $attrs.chart-type or 'valueType'
    sheet           = $scope.sheet

    init-chart!
    draw-chart!

    /*Trigger redraw on window resize*/
    # angular.element $window .bind \resize, ->
    #     draw-chart!
    #     $scope.$apply!

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
        chart-data := sheet[chart-type]
        chart-elem   := $element.find('canvas')[0]
        canvas     := oCanvas.create do
            canvas           : chart-elem
            clear-each-frame : true
            draw-each-frame  : false

        size-canvas!

        slice-proto := canvas.display.arc do
            x           : center-x
            y           : center-y
            radius      : radius
            pie-section : true


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
                       | 'operationType' => $filter('operationTypeStyle') block.type
                       | 'valueType'     => $filter('valueTypeStyle') block.value-type

        /*oCanvas specifies 0 deg as East*/
        last-end = -90

        /*Create a half-pixel overlap to prevent sub-pixel gaps*/
        overlap  = 0.5

        for block in blocks
            start = last-end - overlap
            end   = start + block.angle + overlap
            slice = slice-proto.clone do
                fill         : block.style.fill ?: '#333'
                start        : start
                end          : end
                start-radius : radius

            slice <<<
                duration-days : block.duration-days
                type-name     : block.type-name
                percent       : block.percent-display
                label         : "#{block.duration-days}d\n#{block.type-name}\n#{block.percent-display}"

            /*Create striped overlay if required*/
            if block.style.is_striped
                stripe = slice-proto.clone do
                    fill           : "radial-gradient(center, center, 50% width, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.2), rgba(0, 0, 0, 0))"
                    pointer-events : false
                    start          : start
                    end            : end
                    x              : 0
                    y              : 0

                slice.add-child stripe
                slice.stripe = stripe

            slice
            .bind 'mouseenter touchenter', !->
                label.text = @label
                radius     = @start-radius + 4

                /*Bring current slice to front*/
                @z-index      = 'front'
                mask.z-index  = 'front'
                label.z-index = 'front'

                # Disable animations temporarily
                # $log.log "mouseenter", this
                @radius        = radius
                @stripe.radius = @start-radius if @stripe
                canvas.redraw!

                # @stop!animate do
                #   * radius   : radius
                #   * duration : 250
                #     easing   : 'ease-out-elastic'
                # if @stripe then @stripe.stop!animate do
                #   * radius   : radius
                #   * duration : 250
                #     easing   : 'ease-out-elastic'
                #     queue    : 'stripe-queue'

            .bind 'mouseleave touchleave', !->
                # Disable animations temporarily
                # $log.log "mouseleave", this
                label.text     = ''
                @radius        = @start-radius
                @stripe.radius = @start-radius if @stripe
                canvas.redraw!

                # label.text = ''
                # @stop!animate do
                #   * radius   : @start-radius
                #   * duration : 150
                #   easing     : 'ease-out-quartic'
                # if @stripe then @stripe.stop!animate do
                #   * radius   : @start-radius
                #   * duration : 150
                #     easing   : 'ease-out-quartic'
                #     queue    : 'stripe-queue'


            slices.push slice
            canvas.add-child slice
            last-end = slice.end

        mask = slice-proto.clone do
            pie-section : false
            radius      : Math.floor(center-y - (canvas.width / 4))
            start       : 0
            end         : 360
            fill        : '#fff'

        label = canvas.display.text do
            align          : 'center'
            font           : 'normal 12px Roboto'
            fill           : 'rgba(0, 0, 0, 0.9)'
            origin         : x: 'center', y: 'center'
            pointer-events : false
            x              : center-x
            y              : center-y

        canvas.add-child mask
        canvas.add-child label


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
        canvas.height  = chart-elem.client-height
        center-x      := canvas.width / 2
        center-y      := canvas.height / 2
        radius        := center-y - 10


    /**
     * Calculate the angle of each block
     *
     * @private
     */
    !function size-blocks
        duration = chart-data.duration or 1

        /*Make sure slices have a minimum angle*/
        reserved = blocks.length * min-slice-angle
        ratio    = (360 - reserved) / duration

        for block, i in blocks
            block.angle = Math.floor((block.duration ?: 0) * ratio) + min-slice-angle

        remainder = 360 - _.sum(blocks, 'angle')
        sorted    = _.sort-by blocks, 'duration'

        /*Spread remaining angle across blocks from smallest to largest,
        skipping blocks that are only the minimum slice angle.*/
        while remainder > 0
            for i til sorted.length when sorted[i].angle > min-slice-angle
                continue if remainder is 0
                sorted[i].angle += 1
                remainder       -= 1
