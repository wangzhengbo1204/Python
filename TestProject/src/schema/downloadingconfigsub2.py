#!/usr/bin/env python

#
# Generated Wed Nov 09 16:01:10 2011 by generateDS.py version 2.7a.
#

import sys

import downloadingconfig2 as supermod

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
    def __init__(self, StartTime=None, EndTime=None, Frequency=None, DocCategory=None, WebSetting=None, DatabaseSetting=None, LocalSetting=None):
        super(DownloadingConfigSub, self).__init__(StartTime, EndTime, Frequency, DocCategory, WebSetting, DatabaseSetting, LocalSetting, )
supermod.DownloadingConfig.subclass = DownloadingConfigSub
# end class DownloadingConfigSub


class DatePointSub(supermod.DatePoint):
    def __init__(self, DateType=None, Date=None, DateValue=None, DateUnit=None):
        super(DatePointSub, self).__init__(DateType, Date, DateValue, DateUnit, )
supermod.DatePoint.subclass = DatePointSub
# end class DatePointSub


class WebSettingTypeSub(supermod.WebSettingType):
    def __init__(self, URL=None, Encoding=None, Structe=None, Delimiter=None, Period=None, SearchDateType=None, Step=None):
        super(WebSettingTypeSub, self).__init__(URL, Encoding, Structe, Delimiter, Period, SearchDateType, Step, )
supermod.WebSettingType.subclass = WebSettingTypeSub
# end class WebSettingTypeSub


class PeriodTypeSub(supermod.PeriodType):
    def __init__(self, StartDate=None, EndDate=None):
        super(PeriodTypeSub, self).__init__(StartDate, EndDate, )
supermod.PeriodType.subclass = PeriodTypeSub
# end class PeriodTypeSub


class StepTypeSub(supermod.StepType):
    def __init__(self, ParseSolution=None, Filter=None, MappingID=None, DocType=None, DocTitleIndex=None, DeclearTimeFormat=None, URL=None, XSLT=None, Paging=None):
        super(StepTypeSub, self).__init__(ParseSolution, Filter, MappingID, DocType, DocTitleIndex, DeclearTimeFormat, URL, XSLT, Paging, )
supermod.StepType.subclass = StepTypeSub
# end class StepTypeSub


class FilterTypeSub(supermod.FilterType):
    def __init__(self, SourceType=None, Operation=None, Value=None):
        super(FilterTypeSub, self).__init__(SourceType, Operation, Value, )
supermod.FilterType.subclass = FilterTypeSub
# end class FilterTypeSub


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
    def __init__(self, XSLTFile=None, Param=None, URLType=None, URLTransfer=None):
        super(XSLTTypeSub, self).__init__(XSLTFile, Param, URLType, URLTransfer, )
supermod.XSLTType.subclass = XSLTTypeSub
# end class XSLTTypeSub


class PagingTypeSub(supermod.PagingType):
    def __init__(self, PageTransfer=None, PageNumberName=None):
        super(PagingTypeSub, self).__init__(PageTransfer, PageNumberName, )
supermod.PagingType.subclass = PagingTypeSub
# end class PagingTypeSub


class DatabaseSettingTypeSub(supermod.DatabaseSettingType):
    def __init__(self, DatabaseType=None, ConnectionString=None, DatabaseName=None, TableName=None, Sql=None, Macro=None, MonitorColumn=None, Delimiter=None):
        super(DatabaseSettingTypeSub, self).__init__(DatabaseType, ConnectionString, DatabaseName, TableName, Sql, Macro, MonitorColumn, Delimiter, )
supermod.DatabaseSettingType.subclass = DatabaseSettingTypeSub
# end class DatabaseSettingTypeSub


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
    sys.stdout.write('#from downloadingconfig2 import *\n\n')
    sys.stdout.write('import downloadingconfig2 as model_\n\n')
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


