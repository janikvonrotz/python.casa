import { viteBundler } from '@vuepress/bundler-vite'
import { defaultTheme } from '@vuepress/theme-default'
import { searchPlugin } from '@vuepress/plugin-search'
import { shikiPlugin } from '@vuepress/plugin-shiki'
import { plausiblePlugin } from './plausible'
import { defineUserConfig } from 'vuepress'

export default defineUserConfig({
    bundler: viteBundler(),
    lang: 'de-CH',
    title: 'python.casa',
    description: 'Einführung in die Programmierung.',
    head: [
        ['link', { rel: 'icon', href: '/icon.png' }]
    ],
    theme: defaultTheme({
        logo: 'icon.png',
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
                    { text: 'Thema 11 - Grafische Benutzeroberfläche', link: '/topic-11/' },
                    { text: 'Thema 12 - Webapplikation mit Python Flask', link: '/topic-12/' },
                    { text: 'Thema 13 - Versionskontrolle mit Git', link: '/topic-13/' },
                    { text: 'Thema 14 - Dokumentation mit Markdown', link: '/topic-14/' },
                    { text: 'Thema 15 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-15/' },
                ]
            }
        ],
        sidebar: {
            '/': [
                {
                    text: 'Stundenplan',
                    link: '/timetable.md'
                },
                {
                    text: 'Teil 1',
                    collapsible: true,
                    children: [
                        { text: 'Thema 1 - Einführung Programmiersprache', link: '/topic-1/', collapsible: true, children: ['/topic-1/slides1.md', '/topic-1/excercise1.md'], },
                        { text: 'Thema 2 - Variablen und Datentypen', link: '/topic-2/', collapsible: true, children: ['/topic-2/slides2.md', '/topic-2/excercise2.md'], },
                        { text: 'Thema 3 - Boolsche Algebra und Zeichenketten', collapsible: true, link: '/topic-3/', children: ['/topic-3/slides3.md', '/topic-3/excercise3.md'], },
                        { text: 'Thema 4 - Datum und Zeit', link: '/topic-4/', collapsible: true, children: ['/topic-4/slides4.md', '/topic-4/excercise4.md'], },
                        { text: 'Thema 5 - Kontrollstrukturen und Listen', link: '/topic-5/', collapsible: true, children: ['/topic-5/slides5.md', '/topic-5/excercise5.md'], },
                        { text: 'Thema 6 - Funktionen und Flowcharts', link: '/topic-6/', collapsible: true, children: ['/topic-6/slides6.md', '/topic-6/excercise6.md'], },
                        { text: 'Thema 7 - Objektorientierte Programmierung', link: '/topic-7/', collapsible: true, children: ['/topic-7/slides7.md', '/topic-7/excercise7.md'], },
                        { text: 'Thema 8 - Ein- und Ausgabe', link: '/topic-8/', collapsible: true, children: ['/topic-8/slides8.md', '/topic-8/excercise8.md'], },
                    ]
                },
                {
                    text: 'Teil 2',
                    collapsible: true,
                    children: [
                        { text: 'Thema 9 - Module und Import', link: '/topic-9/', collapsible: true, children: ['/topic-9/slides9.md', '/topic-9/excercise9.md'], },
                        { text: 'Thema 10 - Datenbanken', link: '/topic-10/', collapsible: true, children: ['/topic-10/slides10.md', '/topic-10/excercise10.md'], },
                        { text: 'Thema 11 - Grafische Benutzeroberfläche', link: '/topic-11/', collapsible: true, children: ['/topic-11/slides11.md', '/topic-11/excercise11.md'], },
                        { text: 'Thema 12 - Webapplikation mit Python Flask', link: '/topic-12/', collapsible: true, children: ['/topic-12/slides12.md', '/topic-12/excercise12.md'], },
                        { text: 'Thema 13 - Versionskontrolle mit Git', link: '/topic-13/', collapsible: true, children: ['/topic-13/slides13.md', '/topic-13/excercise13.md'], },
                        { text: 'Thema 14 - Dokumentation mit Markdown', link: '/topic-14/', collapsible: true, children: ['/topic-14/slides14.md'], },
                        { text: 'Thema 15 - Jupiter-Notebooks, SciPy und Matplotlib', link: '/topic-15/', collapsible: true, children: ['/topic-15/slides15.md', '/topic-15/excercise15.md'], },
                    ]
                },                
                {
                    text: 'Prüfung',
                    collapsible: true,
                    // link: 'exam.md',
                    children: ['/exam1.md', '/exam2.md', '/exam3.md']
                }
            ]
        }
    }),
    plugins: [
        searchPlugin(),
        shikiPlugin({ theme: 'dark-plus' }),
        plausiblePlugin({
            'domain': 'python.casa'
        }),
        shikiPlugin({
            theme: 'dark-plus'
        }),
    ],
})
