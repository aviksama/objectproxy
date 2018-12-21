NoneType = type(None)


class ProxyElement(object):
    def __init__(self, func, args, kwargs, parent=None, ca_args=None, ca_kwargs=None, as_method=False):
        self._func = func
        self._value = "__PROXY_NULL_TYPE__"
        self._parent = parent
        self._args = args
        self._kwargs = kwargs
        self._ca_args = ca_args or []
        self._ca_kwargs = ca_kwargs or {}
        self._as_method = as_method

    def __call__(self, *args, **kwargs):
        if self._value != "__PROXY_NULL_TYPE__":
            raise ValueError("cannot make a callable proxy after evaluation")
        self._ca_kwargs = kwargs
        self._ca_args = args
        self._as_method = True
        return self

    def __getattr__(self, item):
        if self._value == "__PROXY_NULL_TYPE__":
            return ProxyElement(lambda value: getattr(value, item), None, None, parent=self)
        return getattr(self._value, item)

    def __getitem__(self, item):
        if self._value == "__PROXY_NULL_TYPE__":
            return ProxyElement(lambda value: value[item], None, None, parent=self)
        return self._value[item]


class MethodProxyElement(object):
    def __new__(cls, func, args, kwargs, ca_args=None, ca_kwargs=None, parent=None):
        return ProxyElement(func, args, kwargs, ca_args=ca_args, ca_kwargs=ca_kwargs, parent=parent, as_method=True)


def eval_proxy(self):
    if not isinstance(self, ProxyElement):
        raise ValueError("argument must be a ProxyElement object")
    if self._value == "__PROXY_NULL_TYPE__" and not self._parent:
        _args = [eval_proxy(arg) if isinstance(arg, ProxyElement) else arg for arg in self._args]
        _kwargs = {k: eval_proxy(v) if isinstance(v, ProxyElement) else v for k, v in self._kwargs.items()}
        self._value = self._func(*_args, **_kwargs)
    elif self._value == "__PROXY_NULL_TYPE__" and self._parent:
        self._value = self._func(eval_proxy(self._parent))
    if self._as_method is True and callable(self._value):
        self._value = self._value(*self._ca_args, **self._ca_kwargs)
    return self._value
