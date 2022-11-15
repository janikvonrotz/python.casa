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
                    { text: 'Thema 4 - Datum und Zeit', link: '/topic-4/' },
                    { text: 'Thema 5 - Kontrollstrukturen und Listen', link: '/topic-5/' },
                    { text: 'Thema 6 - Funktionen und Flowcharts', link: '/topic-6/' },
                    { text: 'Thema 7 - Objektorientierte Programmierung', link: '/topic-7/' },
                    { text: 'Thema 8 - Ein- und Ausgabe', link: '/topic-8/' },
                    { text: 'Thema 9 - Module und Import', link: '/topic-9/' },
                    { text: 'Thema 10 - Datenbanken', link: '/topic-10/' },
                    { text: 'Thema 11 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-11/' },
                    { text: 'Thema 12 - Webapplikation mit Python Flask', link: '/topic-12/' },
                    { text: 'Thema 13 - Versionskontrolle mit Git', link: '/topic-13/' },
                ]
            }
        ],
        sidebar: {
            '/': [
                {
                    text: 'Teil 1',
                    link: 'timetable.md'
                },
                {
                    text: 'Teil 1',
                    collapsible: true,
                    children: [
                        { text: 'Thema 1 - Einführung Programmiersprache', link: '/topic-1/', collapsible: true, children: ['slides1.md', 'excercise1.md'], },
                        { text: 'Thema 2 - Variablen und Datentypen', link: '/topic-2/', collapsible: true, children: ['slides2.md', 'excercise2.md'], },
                        { text: 'Thema 3 - Boolsche Algebra und Zeichenketten', collapsible: true, link: '/topic-3/', children: ['slides3.md', 'excercise3.md'], },
                        { text: 'Thema 4 - Datum und Zeit', link: '/topic-4/', collapsible: true, children: ['slides4.md', 'excercise4.md'], },
                        { text: 'Thema 5 - Kontrollstrukturen und Listen', link: '/topic-5/', collapsible: true, children: ['slides5.md', 'excercise5.md'], },
                        { text: 'Thema 6 - Funktionen und Flowcharts', link: '/topic-6/', collapsible: true, children: ['slides6.md', 'excercise6.md'], },
                        { text: 'Thema 7 - Objektorientierte Programmierung', link: '/topic-7/', collapsible: true, children: ['slides7.md', 'excercise7.md'], },
                        { text: 'Thema 8 - Ein- und Ausgabe', link: '/topic-8/', collapsible: true, children: ['slides8.md', 'excercise8.md'], },
                    ]
                },
                {
                    text: 'Teil 2',
                    collapsible: true,
                    children: [
                        { text: 'Thema 9 - Module und Import', link: '/topic-9/', collapsible: true, children: ['slides9.md', 'excercise9.md'], },
                        { text: 'Thema 10 - Datenbanken', link: '/topic-10/', collapsible: true, children: ['slides10.md', 'excercise10.md'], },
                        { text: 'Thema 11 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-11/', collapsible: true, children: ['slides11.md', 'excercise11.md'], },
                        { text: 'Thema 12 - Webapplikation mit Python Flask', link: '/topic-12/', collapsible: true, children: ['slides12.md', 'excercise12.md'], },
                        { text: 'Thema 13 - Versionskontrolle mit Git', link: '/topic-13/', collapsible: true, children: ['slides13.md', 'excercise13.md'], },
                    ]
                },
                {
                    text: 'Prüfung',
                    collapsible: true,
                    link: 'exam.md',
                    children: [
                        { text: 'Wissenprüfung1', link: 'exam1.md' },
                        { text: 'Wissenprüfung2', link: 'exam2.md' },
                        { text: 'Leistungsnachweis', link: 'exam3.md' },
                        { text: 'Thema 10 - Datenbanken', link: '/topic-10/', collapsible: true, children: ['slides10.md', 'excercise10.md'], },
                        { text: 'Thema 11 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-11/', collapsible: true, children: ['slides11.md', 'excercise11.md'], },
                        { text: 'Thema 12 - Webapplikation mit Python Flask', link: '/topic-12/', collapsible: true, children: ['slides12.md', 'excercise12.md'], },
                        { text: 'Thema 13 - Versionskontrolle mit Git', link: '/topic-13/', collapsible: true, children: ['slides13.md', 'excercise13.md'], },
                    ]
                }
            ]
        }
    }),
    plugins: [
        searchPlugin(),
        plausiblePlugin({
            'domain': 'python.casa'
        })
    ],
}
