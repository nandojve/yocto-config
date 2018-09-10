def __set_defaults_falcon_yocto():
    import os
    import sys

    valid_machines = ['comex']

    local_conf_exists = os.path.isfile(os.path.join(build_dir,
                                                    'conf',
                                                    'local.conf'))

    def required_var_error(varname, valid_vals):
        sys.stderr.write("ERROR: You must set '%s' before setting up the environment.\n" %
                         (varname,))
        sys.stderr.write("       Possible values are %s\n" % valid_vals)
        sys.exit(1)

    def maybe_set_default(varname, valid_vals):
        try:
            val = os.environ[varname]
        except KeyError:
            val = None

        if val:
            if val in valid_vals:
                set_default(varname, val)
            else:
                required_var_error(varname, valid_vals)
        elif not local_conf_exists:
            required_var_error(varname, valid_vals)

    set_default('DISTRO', 'falcon')
    maybe_set_default('MACHINE', valid_machines)

def __after_init_falcon_yocto():
    PLATFORM_ROOT_DIR = os.environ['PLATFORM_ROOT_DIR']

    append_layers([ os.path.join(PLATFORM_ROOT_DIR, 'sources', p) for p in
                    [
                     'meta-falcon',
                     'meta-intel',
                     'meta-mono',
                     'meta-security',
                     'meta-telephony',
                     'meta-virtualization',
                     'meta-openembedded/meta-filesystems',
                     'meta-openembedded/meta-multimedia',
                     'meta-openembedded/meta-networking',
                     'meta-openembedded/meta-oe',
                     'meta-openembedded/meta-perl',
                     'meta-openembedded/meta-python',
                     'meta-openembedded/meta-webserver'
                    ]])

run_set_defaults(__set_defaults_falcon_yocto)
run_after_init(__after_init_falcon_yocto)
