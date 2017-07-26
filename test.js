//start.js
// var spawn = require('child_process').spawn,
//     py    = spawn('python', ['interface.py']),
//     data = ['SPX', ['onyr']]
//
//     metrics = '';
//
// py.stdout.on('data', function(data){
//   metrics += data.toString();
// });
// py.stdout.on('end', function(){
//   console.log('Sum of numbers=',metrics);
// });
// py.stdin.write(JSON.stringify(data));
// py.stdin.end();
//


// python interface.py ticker period,...,period
var exec = require('child_process').exec;
exec('python interface.py SPX onyr,ytd', function(error, stdout, stderr) {
    console.log('stdout: ', stdout);
    console.log('stderr: ', stderr);
    if (error !== null) {
        console.log('exec error: ', error);
    }
});

// var child = require('child_process').exec('python ./compute_input.py [1,2,3,4]')
// child.stdout.pipe(process.stdout)
// child.on('exit', function() {
//   process.exit()
// })
