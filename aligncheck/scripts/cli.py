import click
from .. import check_alignment
from .. import __version__ as aligncheck_version


@click.command(short_help="Check raster alignment.")
@click.argument('inputfiles', type=click.Path(resolve_path=True), required=True,
                nargs=-1, metavar="INPUT")
@click.option('--report/--no-report', default=False)
@click.option('--full-report/--no-full-report', default=False)
@click.option('--header/--no-header', default=True)
@click.version_option(version=aligncheck_version, message='%(version)s')
@click.pass_context
def aligncheck(_, inputfiles, report, full_report, header):
    """
    Check if input rasters are aligned.
    """
    kwargs = dict(report=report, full_report=full_report, header=header)
    result = check_alignment(inputfiles, **kwargs)

    if result:
        for row in result:
            click.echo(row)
    else:
        click.echo('aligned')
