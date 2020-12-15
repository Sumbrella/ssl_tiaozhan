import os


from loguru import logger
from snapshot_phantomjs import snapshot
from pyecharts.render import make_snapshot


def change2pic(data_dir, save_dir):

    files = os.listdir(data_dir)

    if not os.path.exists(os.path.join(save_dir, 'figures')):
        os.mkdir(os.path.join(save_dir, 'figures'))

    for file in files:
        if os.path.isfile(os.path.join(save_dir, file)):
            name, ext = os.path.splitext(file)
            if ext == '.html':
                logger.info(f"saving {file}...")
                make_snapshot(snapshot, os.path.join(save_dir, file), os.path.join(save_dir, 'figures', f"{name}.png"))
                logger.info("save success!")


def main():
    data_dir = os.path.join(os.path.dirname(__file__), 'results')
    results_dir = os.path.join(os.path.dirname(__file__), 'results')
    change2pic(data_dir, results_dir)


if __name__ == '__main__':
    main()
