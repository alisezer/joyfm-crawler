import click
from crawler.spider import JoySpider
import logging

# Logger Setup
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
log_level = 'INFO'
logging.basicConfig(level=log_level, format=log_fmt)
logger = logging.getLogger(__name__)


@click.group()
def manage():
    pass


@click.command()
def single():
    """Single run - save data to csv"""
    JoySpider().single_run()


@click.command()
@click.option('--count', type=int, help='How many times to run')
def counted(count):
    """Counted run - save data to csv"""
    JoySpider().counted_run(count)


@click.command()
@click.option('--days', type=int, help='Days to continue running')
@click.option('--hours', type=int, help='Hours to continue running')
def timed(days, hours):
    """Timed run - save data to  csv"""
    JoySpider().timed_run(days, hours)


manage.add_command(single)
manage.add_command(counted)
manage.add_command(timed)

if __name__ == '__main__':
    manage()
