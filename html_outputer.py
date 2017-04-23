__author__ = 'Administrator'

import sys
reload(sys)


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return

        self.datas.append(data)

    def output_html(self):
        sys.setdefaultencoding('utf8')
        with open('output.html', 'w') as fout:
            fout.write('<html>')
            fout.write('<meta charset="UTF-8">')
            fout.write('<meta http-equiv="content-type" content="text/html;charset=utf-8">')
            fout.write('<body>')
            fout.write('<table>')
            for data in self.datas:
                title = data['title'].encode('utf-8')
                fout.write('<tr>')
                fout.write('<td><a href=%s>%s</a></td>' % (data['url'], title))
                fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))
                fout.write('</tr>')
            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')