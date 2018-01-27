#encoding:utf-8

#    urls模块

urls = (
    '/api', 'api',
    '/users','users',
    '/users(/\d+)', 'users',
    '/redirect', 'redirect',
    '/blog/[0-9a-zA_Z]+', 'blog', 
    '/(.*)', 'index'
)