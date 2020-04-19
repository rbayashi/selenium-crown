FROM python:3

# requirementsのファイルをおくディレクトリを変数に
ADD requirements.txt /root/script/requirements.txt

# vimとseleniumをインストール
RUN set -x && \
  apt-get update && \
  apt-get install -y vim && \
  pip install -r /root/script/requirements.txt
