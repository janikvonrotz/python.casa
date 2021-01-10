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
                { text: 'Thema 1', link: '/topic-1/' },
                { text: 'Thema 2', link: '/topic-2/' },
                { text: 'Thema 3', link: '/topic-3/' },
                { text: 'Thema 4', link: '/topic-4/' },
                { text: 'Thema 5', link: '/topic-5/' },
                { text: 'Thema 6', link: '/topic-6/' },
              ]
            }
          ]
    },
    plugins: [
        '@vuepress/active-header-links',
        '@vuepress/medium-zoom',
        'vuepress-plugin-mermaidjs',
        'plausible-analytics',
        '@vuepress/back-to-top',
        '@vuepress/last-updated'
    ]
}
