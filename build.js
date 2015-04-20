/* jshint node: true */

var ghpages = require('gh-pages');
var path = require('path');

ghpages.publish(path.join(__dirname, 'site'), function(err) {
  console.error(path.join(__dirname, 'site'));
  console.error('Uh-oh! ' + err);
});
