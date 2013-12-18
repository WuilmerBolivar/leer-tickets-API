#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Desarrolladores de Tribus
#
# This file is part of Tribus.
#
# Tribus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tribus is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import time
import json
import urllib2

print '========================'
print 'Tareas pendientes:'
print '========================'
issuesabiertos = 'https://api.github.com/repos/CanaimaGNULinux/tribus/issues?page=1&state=open'
servidor = urllib2.urlopen(issuesabiertos)
js = json.load(servidor)
for tag in js:
	print '* [] Issue: ' + '#' + str(tag['number'])
	print u'\tTítulo: ' + tag['title']
	print '\tCreado: ' + tag['created_at']
	#print u'\tDescripción: ' + tag['body']
	print '\tVer issues: ' + tag['html_url'] + '\n'
print '========================'
print 'Tareas realizadas:'
print '========================'
issuescerrados = 'https://api.github.com/repos/CanaimaGNULinux/tribus/issues?page=1&state=close'
servidor = urllib2.urlopen(issuescerrados)
js = json.load(servidor)
for tag in js:
	print '* [HECHO] Issue: ' + '#' + str(tag['number'])
	print u'\tTítulo: ' + tag['title']
	print '\tCreado: ' + tag['created_at']
	#print u'\tDescripcion: ' + tag['body']
	print '\tVer issues: ' + tag['html_url'] + '\n'
print '========================'
print 'Versiones Tribus:'
print '========================'
milestones = 'https://api.github.com/repos/CanaimaGNULinux/tribus/milestones'
servidor = urllib2.urlopen(milestones)
js = json.load(servidor)
for tag in js:
	print '* Milestone: ' + str(tag['number'])
	print u'\tVersión: ' + tag['title']
	print '\tEstado: ' + tag['state']
	print '\tIssues Abiertos: ' + str(tag['open_issues'])
	print '\tIssues Cerrados: ' + str(tag['closed_issues'])
	print '\tCreado: ' + tag['created_at'] + '\n'
	#print u'\tDescripción: ' + tag['description'] + '\n'
print '========================'
print 'Contribuciones:'
print '========================'
colaboradores = 'https://api.github.com/repos/CanaimaGNULinux/tribus/contributors'
servidor = urllib2.urlopen(colaboradores)
js = json.load(servidor)
for tag in js:
	print '* Usuario: ' + tag['login']
	print '\tContribuciones: ' + str(tag['contributions']) + ' commit(s)'
	print '\tVer colaborador: ' + tag['html_url'] + '\n'
print '========================'
print 'FIN'
print '========================'
time.sleep(10)
