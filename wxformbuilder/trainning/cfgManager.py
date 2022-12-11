import configparser
import sys, os

DEFAULT_CONF = {
    'DEFAULT': { 
        'description': '如题',
        'total_cnt': 0,
        'right_cnt': 0,
        'answer': '出题者很懒，没写答案'
        }
    }


def get_all_cfg_file(conf_dir: str) -> list[str]:
    for _,_, files in os.walk(conf_dir):
        return [cfg_file for cfg_file in files if cfg_file.endswith('.cfg')]


def get_all_cfg_name(conf_dir: str) -> list[str]:
    for _,_, files in os.walk(conf_dir):
        return [cfg_file[:-4] for cfg_file in files if cfg_file.endswith('.cfg')]


def load_from_dir(conf_dir: str):
    cfg = configparser.ConfigParser()
    cfg.read_dict(DEFAULT_CONF)
    
    for cfg_file in get_all_cfg_file(conf_dir):
        cfg.read(os.path.join(conf_dir, cfg_file), encoding = 'utf-8')

    return cfg


def load_from_file(filepath):
    cfg = configparser.ConfigParser()
    cfg.read_dict(DEFAULT_CONF)
    cfg.read(filepath, encoding = 'utf-8')
    return cfg


def update_cfg(cfg_filepath, cfg_instance):
    cfg = configparser.ConfigParser()
    cfg.remove_section('DEFAULT')
    cfg.update(cfg_instance)
    cfg.write(open(cfg_filepath, 'w', encoding = 'utf-8'))
    cfg.read_dict(DEFAULT_CONF)



if __name__ == '__main__':
    print(load_from_dir('conf.d'))