import frappe
from frappe.auth import LoginManager
from werkzeug.utils import redirect

@frappe.whitelist(allow_guest=True)
def custom_login_and_redirect(user, pwd, redirect_to):
    try:
        # Membuat instansi LoginManager dan melakukan login
        login_manager = LoginManager()
        login_manager.authenticate(user=user, pwd=pwd)
        login_manager.post_login()

        # Redirect ke URL tertentu setelah login berhasil
        return redirect(redirect_to)

    except frappe.exceptions.AuthenticationError:
        # Tangani kesalahan otentikasi
        return "Login failed. Invalid email or password."
