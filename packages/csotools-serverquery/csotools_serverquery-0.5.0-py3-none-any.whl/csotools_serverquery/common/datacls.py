"""
Cheap dataclasses module backport

Check out the official documentation to see what this is trying to
achieve:
https://docs.python.org/3/library/dataclasses.html
"""
"""
MIT License

Copyright (c) 2020 Gabriel Huber
Copyright (c) 2022 Anggara Yama Putra

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import collections;
import copy;



class DataclsBase ():
    def __init__ (self, **kwargs):
        for name, value in self._defaults.items():
            if name in kwargs:
                value = kwargs[name];
            setattr( self, name, copy.copy(value) );

    def __iter__(self):
        for name in self.__annotations__:
            yield (name, getattr(self, name));

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ", ".join( name + "=" + repr(value) for name, value in self) );


class DataclsMeta (type):
    def __new__ (cls, name, bases, prop):
        values = collections.OrderedDict();
        for member_name in prop["__annotations__"].keys():
            # Check if member has a default value set as class variable
            if member_name in prop:
                # Store default value and remove the class variable
                values[member_name] = prop[member_name];
                del prop[member_name];
            else:
                # Set None as the default value
                values[member_name] = None;
        prop["__slots__"] = list( values.keys() );
        prop["_defaults"] = values;
        bases = (DataclsBase, *bases);
        return super().__new__( cls, name, bases, prop );

    def __prepare__ (self, *args, **kwargs):
        return collections.OrderedDict();
