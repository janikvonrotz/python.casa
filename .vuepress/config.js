module.exports = {
    title: 'python.casa',
    description: 'Einführung in die Programmierung.',
    themeConfig: {
        sidebar: 'auto',
        repo: 'janikvonrotz/python.casa',
        docsBranch: 'main',
        editLinks: true,

        nav: [
            { text: 'Home', link: '/' },
            {
              text: 'Lektionen',
              ariaLabel: 'Auswahl Lektionen',
              items: [
                { text: 'Thema 1 - Einführung Programmiersprache', link: '/topic-1/' },
                { text: 'Thema 2 - Variablen und Datentypen', link: '/topic-2/' },
                { text: 'Thema 3 - Boolsche Algebra und Zeichenketten', link: '/topic-3/' },
                { text: 'Thema 4 - Kontrollstrukturen und Listen', link: '/topic-4/' },
                { text: 'Thema 5 - Funktionen und Flowcharts', link: '/topic-5/' },
                { text: 'Thema 6 - Ein- und Ausgabe', link: '/topic-6/' },
              ]
            }
          ]
    },
    plugins: [
        'fulltext-search',
        '@vuepress/active-header-links',
        '@vuepress/medium-zoom',
        'vuepress-plugin-mermaidjs',
        'plausible-analytics',
        '@vuepress/back-to-top',
        '@vuepress/last-updated'
    ]
}
