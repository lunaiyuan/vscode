from HTMLTable import HTMLTable
table1 = HTMLTable(caption='运动员管理系统（球员）')
table2 = HTMLTable(caption='运动员管理系统（守门员）')
# 表头行
table1.append_header_rows(
    (('№', '姓名', '握力器', '躺举杠铃', '曲臂悬垂', '仰卧起坐', '引体向上', '模拟滑行', '8字滑行', '8字滑行',
      '射门', '6圈', '折线滑'), ('', '', '右', '左', '成绩', '成绩', '成绩', '成绩',
                           '（不带球）（秒）', '（带球）（秒）', '成绩', '分钟', '秒')))
table1[0][2].attr.colspan = 2
table1[0][0].attr.rowspan = 2
table1[0][1].attr.rowspan = 2

html = table1.to_html()
print(html)