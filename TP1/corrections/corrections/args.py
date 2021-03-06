# -*- coding: utf-8 -*-

from __future__ import print_function

import copy
import pprint

from rendering import commas, truncate_str, truncate_value

####################
class ArgsKeywords(object):
    """
    The most general form of a function argument list is made
    of a tuple and a dictionary
    
    Example:
    my_input = ArgsKeywords( (1,2), {'a': []})
    my_input.call (foo)
    would then return the result of
    foo (1, 2, a=[])
    """
    def __init__(self, args=None, keywords=None):
        # expecting a tuple or a list
        self.args = args if args is not None else tuple()
        # expecting a dictionary
        self.keywords = keywords if keywords is not None else {}
        # can be overridden later on using 'render_function_name'
        self.function_name = None
        # can be overridden later on using 'render_prefix'
        self.prefix = ""
        # default - no way to set this on the constructor
        # because layout=x is already captured in self.keywords
        self.layout = None

    def __repr__(self):
        cn = "Args" if not self.keywords else "ArgsKeywords"
        result = "<Args {}{}{} ".format(self.prefix, self.function_name, self.args)
        if self.keywords:
            result += "Keywords:" + ",".join(["{}={}".format(k, v) for (k, v) in self.keywords.items() ])
        result += ">"
        return result

    def set_layout(self, layout):
        # used when rendering - in exemple or correction
        # in general this is defined in the Exercice instance
        # but can also be overridden here
        self.layout = layout
        
    def call(self, function, debug=False):
        if debug:
            print("calling {} *{} **{}".format(function.__name__, self.args, self.keywords))
        return function(*self.args, **self.keywords)

    def init_obj(self, klass, debug=False):
        if debug:
            print("creating object in class {}, *{} **{}"
                  .format(klass.__name__, self.args, self.keywords))
        return klass(*self.args, **self.keywords)
                  
    def call_obj(self, object, methodname, debug=False):
        if debug:
            print("calling method {} on object {} *{} **{}"
                  .format(methodname, object, self.args, self.keywords))
        method = getattr(object, methodname)
        return method(*self.args, **self.keywords)
                  
    def clone(self, copy_mode):
        "clone this input for safety"
        if copy_mode == 'shallow':
            return copy.copy(self)
        elif copy_mode == 'deep':
            return copy.deepcopy(self)
        else:
            return self

    def render_function_name(self, function_name):
        """
        if called, arguments will be rendered like this
        function_name (arg1, ... argn)
        instead of just
        arg1, .. argn
        """
        self.function_name = function_name
        
    def render_prefix(self, prefix):
        """
        if called, arguments will be rendered like this
        with the prefix prepended
        """
        self.prefix = prefix

    def layout_void(self, width):
        return ""

    def layout_truncate(self, width):
        """
        render a list of arguments on a single line, truncated
        remember that width <= 0 means no truncation
        """
        text = commas(self.args)
        if self.keywords:
            text += ", " + commas(self.keywords)
        if self.function_name:
            text = "{}({})".format(self.function_name, text)
        text = self.prefix + text
        return truncate_str(text, width)
    
    def layout_pprint(self, width):
        """
        render a list of arguments in pprint mode
        """
        # try to render with no width limit, if it fits it's OK
        simple_case = self.layout_truncate(width=0)
        if len(simple_case) <= width:
            #print("using simple_case {}".format(simple_case))
            return simple_case
        else:
            #print("simple_case too long {} > {}".format(len(simple_case), width))
            pass
        # else
        indent = 2
        sep = indent*' '
        html = "<pre>"
        html += self.prefix
        if self.function_name:
            html += self.function_name + "(\n"
        def indent_pformat(pformat_result):
            return sep + pformat_result.replace("\n","\n"+sep)
        args_tokens = [ pprint.pformat(arg, width=width-indent, indent=indent) for arg in self.args ]
        keyword_tokens =  [ "{}={}".format(k,pprint.pformat(v, width=width-indent, indent=indent))
                            for k,v in self.keywords ]
        tokens = [ indent_pformat(x) for x in args_tokens + keyword_tokens ]
        html += (",\n").join(tokens)
        if self.function_name:
            html += ")\n"
        html += "</pre>"
        return html
        
# simplified for when no keywords are required
class Args(ArgsKeywords):
    """
    In most cases though, we do not use keywords so it is more convenient to
    just pass a list of arguments

    Example:
    my_input = Args (1, 2, 3)
    my_input.call(foo)
    would then return the result of
    foo(1, 2, 3)

    Like for ArgKeywords it is preferable to set the layout 
    using the separate set_leyout method
    """
    def __init__(self, *args, **kwds):
        # it is NOT *args here, this is intentional
        ArgsKeywords.__init__(self, args, **kwds)

