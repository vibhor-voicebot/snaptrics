import uuid
import requests
from flask import Flask, render_template, session, request, redirect, url_for
from flask_session import Session  # https://pythonhosted.org/Flask-Session
import msal




from flask import Flask, render_template, request
from flask import Flask, jsonify, request, render_template
import socket, os, json, sys
import requests
import random, os
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
import subprocess
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import mysql
import mysql.connector
import sys, getopt
import pymysql
import subprocess
from subprocess import PIPE, run
import sys,os
from azure.cli.core import get_default_cli
from flask import Flask, jsonify, request, render_template
import socket, os, json, sys
import requests
import random, os
from azure.common.client_factory import get_client_from_cli_profile
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
import subprocess

#Use the get_client_from_auth_file method to create the client object:
from azure.common.client_factory import get_client_from_auth_file
from azure.mgmt.resource import SubscriptionClient
import sys, yaml
from flask import send_file, send_from_directory, safe_join, abort, Response


######## New libs added
import pyodbc
import struct
import adal
from msrestazure.azure_active_directory import AADTokenCredentials


app = Flask(__name__)

from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

@app.route("/")
def index():
    return redirect(url_for("snaptrics"))
      
@app.route("/snaptrics")
def snaptrics():
    return render_template("index.html")


@app.route("/contactus")
def contactus():
    return render_template("contactus.html")


@app.route("/assignRole")
def assignRole() :

    upn = request.args.get("upn")
    role = request.args.get("role")
    
    return "Role is added for user - "+str(upn)+" as - "+str(role)


if __name__ == "__main__":
    app.run(threaded=True)


