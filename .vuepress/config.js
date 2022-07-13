const { defaultTheme } = require('vuepress')
const { searchPlugin } = require('@vuepress/plugin-search')
const { plausiblePlugin } = require('./plausible')

module.exports = {
    lang: 'de-CH',
    title: 'python.casa',
    description: 'Einführung in die Programmierung.',
    theme: defaultTheme({
        logo: 'logo.png',
        repo: 'janikvonrotz/python.casa',
        docsBranch: 'main',
        editLink: true,
        navbar: [
            { text: 'Home', link: '/' },
            {
                text: 'Lektionen',
                children: [
                    { text: 'Thema 1 - Einführung Programmiersprache', link: '/topic-1/' },
                    { text: 'Thema 2 - Variablen und Datentypen', link: '/topic-2/' },
                    { text: 'Thema 3 - Boolsche Algebra und Zeichenketten', link: '/topic-3/' },
                    { text: 'Thema 3.5 - Datum und Zeit', link: '/topic-3-5/' },
                    { text: 'Thema 4 - Kontrollstrukturen und Listen', link: '/topic-4/' },
                    { text: 'Thema 5 - Funktionen und Flowcharts', link: '/topic-5/' },
                    { text: 'Thema 5.5 - Objektorientierte Programmierung', link: '/topic-5-5/' },
                    { text: 'Thema 6 - Ein- und Ausgabe', link: '/topic-6/' },
                    { text: 'Thema 7 - Module und Import', link: '/topic-7/' },
                    { text: 'Thema 7.5 - Datenbanken', link: '/topic-7-5/' },
                    { text: 'Thema 8 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-8/' },
                    { text: 'Thema 9 - Webapplikation mit Python Flask', link: '/topic-9/' },
                    { text: 'Thema 10 - Versionskontrolle mit Git', link: '/topic-10/' },
                ]
            }
        ],
    }),
    plugins: [
        searchPlugin(),
        plausiblePlugin({
            'domain': 'python.casa'
        })
    ],
}