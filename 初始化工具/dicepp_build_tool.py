import os
try:
    import nonebot
    import openpyxl
    import rsa
    import yaml
except ImportError as e:
    assert False, f"当前Python环境缺少必要库\n({e})\n请检查..."

try:
    import git
    assert git.GIT_OK
except (ImportError, AssertionError):
    git_path = os.path.abspath("../PortableGit/bin/git.exe")
    assert os.path.exists(git_path)
    print(f"找不到自带的Git, 使用PortableGit: {git_path}")
    git.refresh(git_path)
assert git.GIT_OK, "Git不可用, 请检查..."

from git.exc import GitCommandError, NoSuchPathError, InvalidGitRepositoryError

def get_choice():
    return input().upper().find("Y") != -1


def is_network_error(err_str: str):
    if "Could not resolve host" in err_str:
        print("解析IP地址失败, 请尝试修改host文件")
    return "errno 10054" in err_str or "Timed out" in err_str or "Could not resolve host" in err_str

base_path = os.path.abspath("..")

# DicePP Source
dpp_path = os.path.join(base_path, "DicePP")
dpp_git_path = "https://github.com/pear-studio/nonebot-dicepp.git"


def setup_dicepp() -> bool:
    dpp_repo = None
    try:
        dpp_repo = git.Repo(dpp_path)
    except (NoSuchPathError, InvalidGitRepositoryError) as e:
        print("DicePP不存在")

    is_latest = False
    if not dpp_repo:
        try:
            print("从GitHub重新拉取DicePP...")
            dpp_repo = git.Repo.clone_from(url=dpp_git_path, to_path=dpp_path)
            fetch_info = dpp_repo.remote().pull()
            for info in fetch_info:
                print(info)
            print("拉取成功!")
            is_latest = True
        except GitCommandError as e:
            if e.stderr and is_network_error(e.stderr):
                print("网络连接异常, 请确认没有开启VPN或代理服务, 并再次重试")
            print(f"拉取DicePP失败... {e.stderr.strip()}")
            return False

    if dpp_repo.is_dirty() and dpp_repo.head.name == "HEAD" and dpp_repo.remote().name == "origin":
        print("检测到DicePP源码被修改, 是否回退? [Y/N]")
        choice = get_choice()
        if choice:
            dpp_repo.head.reset(index=True, working_tree=True)

    if not is_latest:
        try:
            print("从GitHub更新DicePP...")
            fetch_info = dpp_repo.remote().pull()
            for info in fetch_info:
                print(info)
                is_latest = True
            print("更新完成!")
        except GitCommandError as e:
            if e.stderr and is_network_error(e.stderr):
                print("网络连接异常, 请确认没有开启VPN或代理服务, 并再次重试")
            print(e.stderr.strip())

    print("DicePP已获取")
    if not is_latest:
        print("DicePP未更新到最新版, 请稍后单独运行更新 [DicePP].bat再次尝试更新")
    return True


# BotData
data_path = os.path.join(base_path, "BotData")
link_path = os.path.join(dpp_path, "src/plugins/DicePP/Data")


def setup_botdata() -> None:
    data_exist = os.path.exists(data_path)
    link_exist = os.path.exists(link_path)
    if not data_exist:
        print("BotData文件夹不存在, 是否自动创建空文件夹? [Y(推荐)/N]")
        choice = get_choice()
        if choice:
            os.makedirs(data_path)
        data_exist = os.path.exists(data_path)
    if not data_exist:
        print("无法找到BotData, 请自行确定相关资源已准备好")
    else:
        if not link_exist:
            print("DicePP未正确链接到BotData, 是否链接? [Y(推荐)/N]")
            choice = get_choice()
            if choice:
                os.system(f"mklink /j {link_path} {data_path}")
            else:
                print("请自行确定相关资源已准备好")

# gocqhttp
gocq_path = os.path.join(base_path, "go-cqhttp_windows_amd64")
config_temp_path = os.path.abspath("config_template.yml")


def setup_gocqhttp():
    if not os.path.exists(gocq_path):
        print("无法找到gocqhttp, 请自行完成设置")
    config_path = os.path.join(gocq_path, "config.yml")
    if not os.path.exists(config_path):
        os.system(f"copy {config_temp_path} {config_path}")
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.full_load(f)
    if config["account"]["uin"] == 123456789:
        print("请设置QQ账号")
        account = input().strip()
        try:
            int(account)
        except ValueError:
            print(f"输入的账号{account}必须是数字!")
            return

        with open(config_path, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace("123456789", account, 1)
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(text)


def setup_all() -> bool:
    valid = setup_dicepp()
    if valid:
        print("-------- DicePP设置完毕 --------")
        setup_botdata()
        print("-------- BotData设置完毕 --------")
    else:
        return False
    setup_gocqhttp()
    print("-------- gocqhttp设置完毕 --------")
    return True


if __name__ == "__main__":
    if setup_all():
        print("初始化完成!")
    else:
        print("初始化失败!")
