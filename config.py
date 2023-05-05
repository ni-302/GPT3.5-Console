import configparser
import os
import sys

# 変数の設定
config = configparser.ConfigParser()

# configを生成する関数
def config_gen():
    folder_path = os.path.join('config')
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    if os.path.exists(folder_path):
        print(f'{folder_path} フォルダを作成しました。')
    else:
        print(f'{folder_path} フォルダの作成に失敗しました。')
    while True:
        config_token = "YOUR_TOKEN_HERE"
        try:
            user_input = input("OpenAIのトークンを入力してください。: ") 
        except KeyboardInterrupt:
            sys.exit()
        if user_input is not None:
            config_token = user_input
            break
    config['config'] = {
    'OpenAI_Token': f'{config_token}'
    }
    with open('config/config.ini', 'w') as configfile:
        config.write(configfile)
        print('configの生成が完了しました!')

#configparserの設定
path = "config/config.ini"
is_file = os.path.isfile(path)
if is_file:
    config.read("config/config.ini")
    print('Configを読み込みました!')
else:
    print('Configが見つかりません!')
    config_gen()
try:
    token = config.get('config', 'OpenAI_Token')
except configparser.NoSectionError:
    token = "YOUR_TOKEN_HERE"
except configparser.NoOptionError:
    token = "YOUR_TOKEN_HERE"
