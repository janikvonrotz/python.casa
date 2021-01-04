module.exports = {
    title: 'python.casa',
    description: 'Einführung in die Programmierung.',
    themeConfig: {
        sidebar: 'auto',
        repo: 'janikvonrotz/python.casa',
        docsBranch: 'main',
        editLinks: true
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
