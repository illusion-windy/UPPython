log = "{id}-{type}-{msg}"

print(log.format(id=1,type='debug',msg=u'测试连接'))

info = {
    'id':1,
    'type':'debug',
    'msg':u'测试连接'
}
log = "{0[id]}-{0[type]}-{0[msg]}".format(info)
print(log)

log = "{info[id]}-{info[type]}-{info[msg]}".format(info=info)
print(log)

