/**
 * @param {number[]} timeSeries
 * @param {number} duration
 * @return {number}
 */
var findPoisonedDuration = function(timeSeries, duration) {
    if (timeSeries.length === 0) {
        return 0;
    }
    
    let res = 0;
    for(let i = 0; i < timeSeries.length-1; i++ ) {
        res += Math.min(duration, timeSeries[i+1]-timeSeries[i]);
    }
    
    return res+duration;
};