import sys
import warnings

from edwh import get_task
from edwh_pipcompile_plugin.pipcompile_plugin import DEFAULT_SERVER
from invoke import task


@task
def setup(_):
    print("Whitelabel specific setup")


# deprecation zone:

@task(name="compile", aliases=("pip-compile",))
def wl_pip_compile(ctx, path, pypi_server=DEFAULT_SERVER):
    warnings.warn("DEPRECATED! Please use `edwh pip.compile` instead!", category=DeprecationWarning)

    if not path.endswith(".in"):
        # normally, look at requirements.in but for whitelabel look at whitelabel.in and platform.in
        path = [f"{path}/whitelabel.in", f"{path}/platform.in"]

    if not (pip_compile := get_task("pip.compile")):
        print("! pip.compile task not found !", file=sys.stderr)
        return

    return pip_compile(
        ctx,
        path,
        pypi_server=pypi_server,
        combine=True,
    )


@task(name="upgrade", aliases=("pip-upgrade",))
def wl_pip_upgrade(ctx, path, package=None, force=False, pypi_server=DEFAULT_SERVER):
    warnings.warn("DEPRECATED! Please use `edwh pip.upgrade` instead!", category=DeprecationWarning)

    if not path.endswith(".in"):
        # normally, look at requirements.in but for whitelabel look at whitelabel.in and platform.in
        path = [f"{path}/whitelabel.in", f"{path}/platform.in"]

    if not (pip_upgrade := get_task("pip.upgrade")):
        print("! pip.upgrade task not found !", file=sys.stderr)
        return

    return pip_upgrade(
        ctx,
        path,
        package=package,
        force=force,
        pypi_server=pypi_server,
        combine=True,
    )
