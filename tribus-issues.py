#!/usr/bin/python
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

import json
import urllib2

print '========================'
print 'Tareas pendientes'
print '========================'
issuesabiertos = 'https://api.github.com/repos/CanaimaGNULinux/tribus/issues?page=1&state=open'
servidor = urllib2.urlopen(issuesabiertos)
js = json.load(servidor)
for tag in js:
	print '* [] Issue: ' + '#' + str(tag['number'])
	print 'Titulo: ' + tag['title']
	print 'Creado: ' + tag['created_at']
	print 'Descripcion: ' + tag['body']
	print 'Ver issues: ' + tag['html_url']
	print ''
print ''
print '========================'
print 'Tareas realizadas'
print '========================'
issuescerrados = 'https://api.github.com/repos/CanaimaGNULinux/tribus/issues?page=1&state=close'
servidor = urllib2.urlopen(issuescerrados)
js = json.load(servidor)
for tag in js:
	print '* [HECHO] Issue: ' + '#' + str(tag['number'])
	print 'Titulo: ' + tag['title']
	print 'Creado: ' + tag['created_at']
	print 'Descripcion: ' + tag['body']
	print 'Ver issues: ' + tag['html_url']
	print ''
print ''
print '========================'
print 'Versiones Tribus'
print '========================'
milestones = 'https://api.github.com/repos/CanaimaGNULinux/tribus/milestones'
servidor = urllib2.urlopen(milestones)
js = json.load(servidor)
for tag in js:
	print 'Milestone: ' + str(tag['number'])
	print 'Titulo: ' + tag['title']
	print 'Estado: ' + tag['state']
	print 'Issues Abiertos: ' + str(tag['open_issues'])
	print 'Issues Cerrados: ' + str(tag['closed_issues'])
	print 'Creado: ' + tag['created_at']
	print 'Ver milestones: ' + tag['url']
	print ''
print ''
print '========================'
print 'Contribuciones'
print '========================'
colaboradores = 'https://api.github.com/repos/CanaimaGNULinux/tribus/contributors'
servidor = urllib2.urlopen(colaboradores)
js = json.load(servidor)
for tag in js:
	print 'Usuario: ' + tag['login']
	print 'Contribuciones: ' + str(tag['contributions']) + ' commit(s)'
	print 'Ver colaborador: ' + tag['html_url']
	print ''
