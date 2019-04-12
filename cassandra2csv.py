#!/usr/bin/env python
# coding: UTF-8

import os

class cassandra2csv(object):

    def __validate(self, vls):
        if not os.path.isdir(vls['output_dir']):
            return (False,"You must set an output directoty")

        return (True, "ok")

    @classmethod
    def export(cls, result, max_file_size=0, output_dir=None,
               filename="output.csv", separator=","):

        validate, reason = me.__validate(locals())

        if not validate:
            raise Exception(reason)

        # prepare filename.
        filename = str(filename).replace(" ", "")
        if filename.endswith('.csv'):
            filename = "%s.csv" % filename

        s_fn = filename.split(".csv")
        csv_file = ""

        colnames = result.column_names
        for row in result:
            print(row)
            for colname in colnames:
                print(row.__getattribute__(colname))
            raw_input()

        return True


# create a class instance
me = cassandra2csv()
~                     
