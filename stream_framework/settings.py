from stream_framework.default_settings import *

'''
Please fork and add hooks to import your custom settings system.
Right now we only support Django, but the intention is to support
any settings system.
'''

def update_settings(settings):
    '''Updates stream_frameworks settings using a settings dictionary.
    '''
    for k in settings:
        globals()[k] = settings[k]

def import_global_module(module, current_locals, current_globals, exceptions=None):
    '''Import the requested module into the global scope
    Warning! This will import your module into the global scope.

    **Example**:
        from django.conf import settings
        import_global_module(settings, locals(), globals())

    :param module: the module which to import into global scope
    :param current_locals: the local globals
    :param current_globals: the current globals
    :param exceptions: the exceptions which to ignore while importing
    '''
    try:
        try:
            objects = getattr(module, '__all__', dir(module))

            for k in objects:
                if k and k[0] != '_':
                    current_globals[k] = getattr(module, k)
        except exceptions as e:
            return e
    finally:
        del current_globals, current_locals

# Try importing various webframeworks
try:
    import django
    settings_system = 'django'
except ImportError as e:
    settings_system = None

try:
    import pyramid
    settings_system = 'pyramid'
except ImportError as e:
    setting_system = None

# Update the settings depending on which framework is present
if settings_system == 'django':
    from django.conf import settings
    import_global_module(settings, locals(), globals())
    
elif settings_system == 'pyramid':
    # Call Update settings from withing your Pyramid app's main()
    pass
