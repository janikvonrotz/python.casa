const fs = require('fs')
const glob = require('glob')

/* arguments:
all
sitemap
*/

// settings
const scheme = 'https://'
const hostname = 'python.casa'
const basePath = '/'
const uriSuffix = '.html'

// function sanitizeName(name) {
//     return name.toLocaleLowerCase()
//         .replace(/\s+/g, '-')
//         .replace(/%20/g, '-')
//         .replace('---', '-')
//         .replace('--', '-')
//         .replace(/%c3%84/g, 'ä')
//         .replace(/%c3%bc/g, 'ü')
//         .replace(/%c3%a4/g, 'ä')
//         .replace(/%c3%9c/g, 'ü')
//         .replace(/%c3%b6/g, 'ö')
// }

// Build vars
var args = process.argv.slice(2);
var firstArg = args[0]

if (!firstArg || ['all', 'sitemap'].indexOf(firstArg) > 0) {

    // log
    console.log('Build sitemap ...')

    content = []
    files = [].concat(glob.sync('*.md'), (glob.sync('!(node_modules)**/*.md')))
    files.forEach((file) => {
        content.push(`${scheme}${hostname}${basePath}${file.replace('\.md', '')}${uriSuffix}\n`.replace('README.html',''))
    })

    // write content to index file
    fs.writeFileSync('.vuepress/public/sitemap.txt', content.join(''), 'utf8')

    // log
    console.log('Building sitemap finished.')
}