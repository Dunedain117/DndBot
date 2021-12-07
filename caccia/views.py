from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from Bot.models import Hunter, Captain, Key, Bot_Table
from django.http import HttpResponse
from django.template import RequestContext
from wsgiref.util import FileWrapper
from django.http import JsonResponse
from django.views import View
from telegram import Update as telegramUpdate
from telegram import Bot as telegramBot
from Bot.bot_thread import BotUpdateQueue
from django.apps import apps
import Bot.utils as utils
import os
import json
import sys
import logging

class webhook(View):
    def post(self, request, *args, **kwargs):
        get_update(request.body)
        return JsonResponse({"ok": "POST request processed"})


def get_update(text):
    bot = telegramBot(Bot_Table.objects.first().token)
    update = telegramUpdate.de_json(json.loads(text), bot)
    update_queue = BotUpdateQueue().queue
    update_queue.put(update)

