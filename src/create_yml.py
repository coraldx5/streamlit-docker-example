import csv
import yaml
from streamlit_authenticator.utilities.hasher import Hasher

USERS_CSV_PATH = "config/st_users.csv"
CONFIG_YAML_PATH = "config/st_config.yml"


def load_users(csv_path):
    """
    指定したCSVファイルからユーザー情報を読み込み、辞書のリストとして返します。
    :param csv_path: ユーザー情報CSVファイルのパス
    :return: ユーザー情報のリスト
    """
    with open(csv_path, "r") as f:
        return list(csv.DictReader(f))


def load_yaml(yaml_path):
    """
    指定したYAMLファイルを読み込み、辞書として返します。
    :param yaml_path: YAMLファイルのパス
    :return: YAMLデータの辞書
    """
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)


def hash_users(users):
    """
    ユーザーリスト内の各ユーザーのパスワードをハッシュ化し、
    Streamlit Authenticator用の辞書形式に変換して返します。
    :param users: ユーザー情報のリスト
    :return: ハッシュ化済みユーザー情報の辞書
    """
    users_dict = {}
    for user in users:
        user["password"] = Hasher.hash(user["password"])
        users_dict[user["id"]] = {
            "name": user["name"],
            "password": user["password"],
            "email": user["email"],
        }
    return users_dict


def save_yaml(yaml_path, yaml_data):
    """
    指定した辞書データをYAMLファイルとして保存します。
    :param yaml_path: 保存先YAMLファイルのパス
    :param yaml_data: 保存する辞書データ
    """
    with open(yaml_path, "w") as f:
        yaml.dump(yaml_data, f)
    print("完了")


def main():
    """
    ユーザーCSVを読み込み、パスワードをハッシュ化してYAML設定ファイルに保存します。
    """
    users = load_users(USERS_CSV_PATH)
    yaml_data = load_yaml(CONFIG_YAML_PATH)
    yaml_data["credentials"]["usernames"] = hash_users(users)
    save_yaml(CONFIG_YAML_PATH, yaml_data)


if __name__ == "__main__":
    main()
