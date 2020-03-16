'use strict'

angular.module 'mapping.accounts.services'
    .factory 'WorkPeriodsService', work-periods-service

work-periods-service.$inject = <[ $log Restangular ]>
function work-periods-service ($log, Restangular)
    return new class WorkPeriods
        /**
         * WorkPeriodsService
         * @memberof mapping.accounts.services.WorkPeriodsService
         */
        ->
            @work-periods = Restangular.all \work_periods
                .with-http-config cache: true
                .get-list!
                .then (periods) ~>
                    _.each periods, (period) ->
                        period.shifts-by-days = _group-shifts-by-day period


        /**
         * Retrieve all WorkPeriods for the current users' Company
         * @memberof mapping.accounts.services.WorkPeriodsService
         * @returns {Promise}
         */
        all: -> @work-periods


    /**
     * Map WorkShifts for use with Operations calculations
     * @memberof mapping.accounts.services.WorkPeriodsService
     * @param {Object} period - The WorkPeriod to be mapped
     */
    function _group-shifts-by-day (period)
        /*Initialize days object so all days of the week exist*/
        days = {[i, []] for i in [0 to 6]}
        _.each period.work_shifts, (shift) ->
            days[shift.day_of_week].push do
                start: shift.time_shift_starts
                end: shift.time_shift_ends

        return days
