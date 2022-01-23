
// let points = [[10, 16], [2, 8], [1, 6], [7, 12]];
// 2
// let points = [[1, 2], [3, 4], [5, 6], [7, 8]];
// 4
let points = [[1, 2], [2, 3], [3, 4], [4, 5]];
// 2

var findMinArrowShots = function (points) {
    points = points.sort((a, b) => a[1] - b[1]);
    // console.log(points);
    let shots = 0, end = Number.NEGATIVE_INFINITY;
    for (let [a, b] of points) {
        if (a > end) {
            shots++;
            end = b;
        }
        // console.log(`${a}, ${b}`);
    }
    return shots;
}

console.log(findMinArrowShots(points));
