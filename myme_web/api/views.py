from django.http import HttpResponse

# Create your views here.
def response(request, question):
    # TODO
    #  1．チャットボット用構文解析(JanomeかKotoha)
    #  1-1. kotohaなら必要ないけど、機械学習しなきゃ
    #  2．レスポンス用のdb接続
    #  3．html形式に変換する
    # やること多いっすねʕ◔ϖ◔ʔ

    reply = ""
    if(question):
        reply = "工事中だぜ。<br/>「{0}」には返答できないぜ。".format(question)
    return HttpResponse(reply)