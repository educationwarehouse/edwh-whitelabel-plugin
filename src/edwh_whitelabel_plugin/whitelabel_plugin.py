import io

from invoke import task
from edwh_pipcompile_plugin.pipcompile_plugin import DEFAULT_SERVER
from edwh_pipcompile_plugin.pipcompile_plugin import compile_infile as pip_compile
from edwh_pipcompile_plugin.pipcompile_plugin import upgrade as pip_upgrade


@task(aliases=("pip-compile",))
def compile(ctx, path, pypi_server=DEFAULT_SERVER):
    if not path.endswith(".in"):
        # normally, look at requirements.in but for whitelabel look at whitelabel.in and platform.in
        path = [f"{path}/whitelabel.in", f"{path}/platform.in"]

    return pip_compile(
        ctx,
        path,
        pypi_server=pypi_server,
    )


@task(aliases=("pip-upgrade",))
def upgrade(ctx, path, package=None, force=False, pypi_server=DEFAULT_SERVER):
    if not path.endswith(".in"):
        # normally, look at requirements.in but for whitelabel look at whitelabel.in and platform.in
        path = [f"{path}/whitelabel.in", f"{path}/platform.in"]

    return pip_upgrade(
        ctx,
        path,
        package=package,
        force=force,
        pypi_server=pypi_server,
    )
