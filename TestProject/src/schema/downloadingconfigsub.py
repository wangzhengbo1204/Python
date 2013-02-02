#!/usr/bin/env python

#
# Generated Wed Nov 09 11:52:23 2011 by generateDS.py version 2.7a.
#

import sys

import downloadingconfig as supermod

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError("Failed to import ElementTree from any known place")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#

class DownloadingConfigSub(supermod.DownloadingConfig):
    def __init__(self, StartTime=None, EndTime=None, Frequency=None, WebSetting=None, DatabaseSetting=None, LocalSetting=None, DocCategory=None):
        super(DownloadingConfigSub, self).__init__(StartTime, EndTime, Frequency, WebSetting, DatabaseSetting, LocalSetting, DocCategory, )
supermod.DownloadingConfig.subclass = DownloadingConfigSub
# end class DownloadingConfigSub


class WebSettingTypeSub(supermod.WebSettingType):
    def __init__(self, URL=None, Encoding=None, ParseSolution=None, Structe=None, Delimiter=None, Period=None, SearchByDateType=None, Step=None):
        super(WebSettingTypeSub, self).__init__(URL, Encoding, ParseSolution, Structe, Delimiter, Period, SearchByDateType, Step, )
supermod.WebSettingType.subclass = WebSettingTypeSub
# end class WebSettingTypeSub


class PeriodTypeSub(supermod.PeriodType):
    def __init__(self, StartDate=None, EndDate=None):
        super(PeriodTypeSub, self).__init__(StartDate, EndDate, )
supermod.PeriodType.subclass = PeriodTypeSub
# end class PeriodTypeSub


class StartDateTypeSub(supermod.StartDateType):
    def __init__(self, Type=None, Value=None):
        super(StartDateTypeSub, self).__init__(Type, Value, )
supermod.StartDateType.subclass = StartDateTypeSub
# end class StartDateTypeSub


class EndDateTypeSub(supermod.EndDateType):
    def __init__(self, Type=None, Value=None):
        super(EndDateTypeSub, self).__init__(Type, Value, )
supermod.EndDateType.subclass = EndDateTypeSub
# end class EndDateTypeSub


class SearchByDateTypeTypeSub(supermod.SearchByDateTypeType):
    def __init__(self):
        super(SearchByDateTypeTypeSub, self).__init__()
supermod.SearchByDateTypeType.subclass = SearchByDateTypeTypeSub
# end class SearchByDateTypeTypeSub


class StepTypeSub(supermod.StepType):
    def __init__(self, Filter=None, MappingID=None, DocType=None, DocTitle=None, URL=None, XSLT=None, Paging=None, DeclearTimeFormat=None):
        super(StepTypeSub, self).__init__(Filter, MappingID, DocType, DocTitle, URL, XSLT, Paging, DeclearTimeFormat, )
supermod.StepType.subclass = StepTypeSub
# end class StepTypeSub


class FilterTypeSub(supermod.FilterType):
    def __init__(self, SourceType=None, Operation=None, Value=None):
        super(FilterTypeSub, self).__init__(SourceType, Operation, Value, )
supermod.FilterType.subclass = FilterTypeSub
# end class FilterTypeSub


class SourceTypeSub(supermod.SourceType):
    def __init__(self):
        super(SourceTypeSub, self).__init__()
supermod.SourceType.subclass = SourceTypeSub
# end class SourceTypeSub


class MappingIDTypeSub(supermod.MappingIDType):
    def __init__(self, MarketCode=None, DestinationTypes=None, Source=None):
        super(MappingIDTypeSub, self).__init__(MarketCode, DestinationTypes, Source, )
supermod.MappingIDType.subclass = MappingIDTypeSub
# end class MappingIDTypeSub


class ValueTypeSub(supermod.ValueType):
    def __init__(self, Xpath=None, Title=None, DefaultValue=None):
        super(ValueTypeSub, self).__init__(Xpath, Title, DefaultValue, )
supermod.ValueType.subclass = ValueTypeSub
# end class ValueTypeSub


class DocTypeTypeSub(supermod.DocTypeType):
    def __init__(self, Default=None, Convert=None):
        super(DocTypeTypeSub, self).__init__(Default, Convert, )
supermod.DocTypeType.subclass = DocTypeTypeSub
# end class DocTypeTypeSub


class XSLTTypeSub(supermod.XSLTType):
    def __init__(self, XSLTFile=None, XSLTParams=None, XSLTFileURLExec=None):
        super(XSLTTypeSub, self).__init__(XSLTFile, XSLTParams, XSLTFileURLExec, )
supermod.XSLTType.subclass = XSLTTypeSub
# end class XSLTTypeSub


class XSLTParamsTypeSub(supermod.XSLTParamsType):
    def __init__(self, Param=None):
        super(XSLTParamsTypeSub, self).__init__(Param, )
supermod.XSLTParamsType.subclass = XSLTParamsTypeSub
# end class XSLTParamsTypeSub


class XSLTFileURLExecTypeSub(supermod.XSLTFileURLExecType):
    def __init__(self, ExecType=None, ExecValue=None):
        super(XSLTFileURLExecTypeSub, self).__init__(ExecType, ExecValue, )
supermod.XSLTFileURLExecType.subclass = XSLTFileURLExecTypeSub
# end class XSLTFileURLExecTypeSub


class PagingTypeSub(supermod.PagingType):
    def __init__(self, JSFunc=None, PageNumberName=None):
        super(PagingTypeSub, self).__init__(JSFunc, PageNumberName, )
supermod.PagingType.subclass = PagingTypeSub
# end class PagingTypeSub


class DatabaseSettingTypeSub(supermod.DatabaseSettingType):
    def __init__(self, DatabaseType=None, ConnectionString=None, DatabaseName=None, TableName=None, Sql=None, Macro=None, MonitorColumn=None, Delimiter=None):
        super(DatabaseSettingTypeSub, self).__init__(DatabaseType, ConnectionString, DatabaseName, TableName, Sql, Macro, MonitorColumn, Delimiter, )
supermod.DatabaseSettingType.subclass = DatabaseSettingTypeSub
# end class DatabaseSettingTypeSub


class SqlTypeSub(supermod.SqlType):
    def __init__(self):
        super(SqlTypeSub, self).__init__()
supermod.SqlType.subclass = SqlTypeSub
# end class SqlTypeSub


class LocalSettingTypeSub(supermod.LocalSettingType):
    def __init__(self, Path=None, FilenamePattern=None):
        super(LocalSettingTypeSub, self).__init__(Path, FilenamePattern, )
supermod.LocalSettingType.subclass = LocalSettingTypeSub
# end class LocalSettingTypeSub



def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    if hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DownloadingConfig'
        rootClass = supermod.DownloadingConfig
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    doc = None
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DownloadingConfig'
        rootClass = supermod.DownloadingConfig
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='')
    return rootObj


def parseLiteral(inFilename):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'DownloadingConfig'
        rootClass = supermod.DownloadingConfig
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from downloadingconfig import *\n\n')
    sys.stdout.write('import downloadingconfig as model_\n\n')
    sys.stdout.write('rootObj = model_.DownloadingConfig(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_="DownloadingConfig")
    sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    root = parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()


