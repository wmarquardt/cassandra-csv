#!/usr/bin/env python
# coding: UTF-8

import os
import re
import csv

class CassandraCsv(object):

    filename = ""
    clean_filename = ""
    output_dir = ""
    create_subfolder = False

    def __validate(self, vls):
        if not os.path.isdir(vls['output_dir']):
            return (False,"You must set an output directory")


        return (True, "ok")

    @classmethod
    def export(cls, result, max_file_size=0, output_dir=None,
               filename="output", separator=",", with_header=True,
               create_subfolder=False):

        validate, reason = me.__validate(locals())

        if not validate:
            raise Exception(reason)

        # prepare filename.
        filename = re.sub(r'\.csv$', '', filename)
        me.clean_filename = filename
        if max_file_size:
            filename += """_%(partition)s"""
        me.file_pool = 0 # set counter to 0 when call export
        me.max_file_size = max_file_size
        me.output_dir = output_dir
        me.filename = filename
        me.create_subfolder = create_subfolder
        colnames = result.column_names
        header = [x.title() for x in colnames]
        write_list = []

        write_list.append(header)
        for row in result:
            write_list.append(list(row))
            if max_file_size and\
             len(write_list) >= max_file_size:
                me.__write(write_list)
                write_list = [header]


        if len(write_list) > 1:
            me.__write(write_list)


    def __write(self, to_file):
        self.file_pool += 1
        _path = self.output_dir
        if self.create_subfolder:
            _path = os.path.join(_path, self.clean_filename)
            try:
                os.mkdir(_path)
            except:
                pass

        if self.max_file_size:
            _file = os.path.join(_path,
                                 "%s.csv" % (self.filename % {'partition': self.file_pool} ))
        else:
            _file = os.path.join(_path,"%s.csv" % self.filename)

        with open(_file, 'w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(to_file)

        csvFile.close()
        return _file


# create a class instance
me = CassandraCsv()
