from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    ConversationHandler,
)

# ========================
# CONFIGURACIÓN
# ========================
TOKEN = "7624051682:AAG6pho5cpWc5iQCBeFFnYbBGaBpvjVPGoY"
ADMIN_CHAT_ID = 7555641067  # Chat ID del admin
GROUP_LINK = "https://t.me/+jisBlz-w7Ms0MGZh"

SELECT_LANG = 0

# ========================
# MENSAJES MULTI-IDIOMA
# ========================
MESSAGES = {
    "es": {
        "welcome": "👋 ¡Hola {user}! Bienvenido al bot.\n\nSelecciona una opción:",
        "price": "💰 *Precio único:*\n\n- Plan: $2.99",
        "methods": "💳 *Métodos de pago disponibles:*",
        "usdt": "🪙 *USDT (BEP20)*\nEnvía el pago a esta dirección:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nPresiona el botón de abajo una vez hayas hecho el pago.",
        "paypal": "💵 *PayPal*\nEnvía el pago a este usuario:\n`cizar19`\n\nPresiona el botón de abajo una vez hayas hecho el pago.",
        "waiting": "⏳ Tu pago fue confirmado, en breve se te agrega al grupo: {group}",
        "buttons": ["💰 Ver precios", "💳 Métodos de pago"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ He realizado el pago",
        "pay_now_button": "💸 Realizar pago",
        "admin_confirm_button": "✅ Confirmar pago",
    },
    "en": {
        "welcome": "👋 Hello {user}! Welcome to the bot.\n\nChoose an option:",
        "price": "💰 *Single price:*\n\n- Plan: $2.99",
        "methods": "💳 *Available payment methods:*",
        "usdt": "🪙 *USDT (BEP20)*\nSend the payment to this address:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nPress the button below once you have paid.",
        "paypal": "💵 *PayPal*\nSend the payment to this user:\n`cizar19`\n\nPress the button below once you have paid.",
        "waiting": "⏳ Your payment has been confirmed; you will be added to the group shortly: {group}",
        "buttons": ["💰 View price", "💳 Payment methods"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ I have made the payment",
        "pay_now_button": "💸 Make payment",
        "admin_confirm_button": "✅ Confirm payment",
    },
    "fr": {
        "welcome": "👋 Bonjour {user} ! Bienvenue sur le bot.\n\nSélectionnez une option:",
        "price": "💰 *Prix unique:*\n\n- Plan: $2.99",
        "methods": "💳 *Méthodes de paiement disponibles:*",
        "usdt": "🪙 *USDT (BEP20)*\nEnvoyez le paiement à cette adresse:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nAppuyez sur le bouton ci-dessous une fois le paiement effectué.",
        "paypal": "💵 *PayPal*\nEnvoyez le paiement à cet utilisateur:\n`cizar19`\n\nAppuyez sur le bouton ci-dessous une fois le paiement effectué.",
        "waiting": "⏳ Votre paiement a été confirmé ; vous serez ajouté au groupe sous peu : {group}",
        "buttons": ["💰 Voir le prix", "💳 Méthodes de paiement"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ J'ai effectué le paiement",
        "pay_now_button": "💸 Payer maintenant",
        "admin_confirm_button": "✅ Confirmer le paiement",
    },
    "de": {
        "welcome": "👋 Hallo {user}! Willkommen beim Bot.\n\nWähle eine Option:",
        "price": "💰 *Einzelpreis:*\n\n- Plan: $2.99",
        "methods": "💳 *Verfügbare Zahlungsmethoden:*",
        "usdt": "🪙 *USDT (BEP20)*\nSende die Zahlung an diese Adresse:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nDrücke den Knopf unten, sobald du bezahlt hast.",
        "paypal": "💵 *PayPal*\nSende die Zahlung an diesen Benutzer:\n`cizar19`\n\nDrücke den Knopf unten, sobald du bezahlt hast.",
        "waiting": "⏳ Deine Zahlung wurde bestätigt; du wirst in Kürze zur Gruppe hinzugefügt: {group}",
        "buttons": ["💰 Preis anzeigen", "💳 Zahlungsmethoden"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ Ich habe die Zahlung durchgeführt",
        "pay_now_button": "💸 Bezahlen",
        "admin_confirm_button": "✅ Zahlung bestätigen",
    },
    "it": {
        "welcome": "👋 Ciao {user}! Benvenuto nel bot.\n\nSeleziona un'opzione:",
        "price": "💰 *Prezzo unico:*\n\n- Piano: $2.99",
        "methods": "💳 *Metodi di pagamento disponibili:*",
        "usdt": "🪙 *USDT (BEP20)*\nInvia il pagamento a questo indirizzo:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nPremi il pulsante qui sotto una volta effettuato il pagamento.",
        "paypal": "💵 *PayPal*\nInvia il pagamento a questo utente:\n`cizar19`\n\nPremi il pulsante qui sotto una volta effettuato il pagamento.",
        "waiting": "⏳ Il tuo pagamento è stato confermato; verrai aggiunto al gruppo a breve: {group}",
        "buttons": ["💰 Visualizza prezzo", "💳 Metodi di pagamento"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ Ho effettuato il pagamento",
        "pay_now_button": "💸 Paga ora",
        "admin_confirm_button": "✅ Conferma pagamento",
    },
    "pt": {
        "welcome": "👋 Olá {user}! Bem-vindo ao bot.\n\nSelecione uma opção:",
        "price": "💰 *Preço único:*\n\n- Plano: $2.99",
        "methods": "💳 *Métodos de pagamento disponíveis:*",
        "usdt": "🪙 *USDT (BEP20)*\nEnvie o pagamento para este endereço:\n`0xd2b32183475525c0fa4079a32fc61daccba462bd`\n\nPressione o botão abaixo assim que tiver pago.",
        "paypal": "💵 *PayPal*\nEnvie o pagamento para este usuário:\n`cizar19`\n\nPressione o botão abaixo assim que tiver pago.",
        "waiting": "⏳ Seu pagamento foi confirmado; você será adicionado ao grupo em breve: {group}",
        "buttons": ["💰 Ver preço", "💳 Métodos de pagamento"],
        "paypal_button": "💵 PayPal",
        "usdt_button": "🪙 USDT (BEP20)",
        "confirm_button": "✅ Eu fiz o pagamento",
        "pay_now_button": "💸 Pagar agora",
        "admin_confirm_button": "✅ Confirmar pagamento",
    }
}

# ========================
# /START
# ========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇪🇸 Español", callback_data="lang_es"),
            InlineKeyboardButton("🇺🇸 English", callback_data="lang_en"),
        ],
        [
            InlineKeyboardButton("🇫🇷 Français", callback_data="lang_fr"),
            InlineKeyboardButton("🇩🇪 Deutsch", callback_data="lang_de"),
        ],
        [
            InlineKeyboardButton("🇮🇹 Italiano", callback_data="lang_it"),
            InlineKeyboardButton("🇵🇹 Português", callback_data="lang_pt"),
        ],
    ]
    await update.message.reply_text(
        "🌍 Selecciona tu idioma / Select your language:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return SELECT_LANG

# ========================
# Selección de idioma
# ========================
async def select_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang
    user = query.from_user.first_name
    msg = MESSAGES[lang]

    keyboard = [
        [InlineKeyboardButton(msg["buttons"][0], callback_data="precios")],
        [InlineKeyboardButton(msg["buttons"][1], callback_data="pagos")],
    ]
    await query.edit_message_text(
        msg["welcome"].format(user=user),
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END

# ========================
# Manejo de botones
# ========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "es")
    msg = MESSAGES[lang]

    # Ver precio
    if query.data == "precios":
        keyboard = [[InlineKeyboardButton(msg["pay_now_button"], callback_data="pagos")]]
        await query.edit_message_text(msg["price"], reply_markup=InlineKeyboardMarkup(keyboard))

    # Métodos de pago
    elif query.data == "pagos":
        keyboard = [
            [InlineKeyboardButton(msg["usdt_button"], callback_data="usdt")],
            [InlineKeyboardButton(msg["paypal_button"], callback_data="paypal")]
        ]
        await query.edit_message_text(msg["methods"], reply_markup=InlineKeyboardMarkup(keyboard))

    # Mostrar instrucciones de pago
    elif query.data in ["usdt", "paypal"]:
        text = msg["usdt"] if query.data == "usdt" else msg["paypal"]
        keyboard = [[InlineKeyboardButton(msg["confirm_button"], callback_data="confirm_payment")]]
        await query.edit_message_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    # Cliente confirma pago
    elif query.data == "confirm_payment":
        user = query.from_user
        admin_keyboard = [[InlineKeyboardButton(msg["admin_confirm_button"], callback_data=f"admin_confirm_{user.id}")]]
        admin_text = f"📩 El usuario @{user.username if user.username else user.first_name} ha realizado el pago."
        await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=admin_text, reply_markup=InlineKeyboardMarkup(admin_keyboard))
        await query.edit_message_text("⏳ Espera mientras tu pago es validado...")

    # Admin confirma pago
    elif query.data.startswith("admin_confirm_"):
        user_id = int(query.data.split("_")[-1])
        await context.bot.send_message(chat_id=user_id, text=msg["waiting"].format(group=GROUP_LINK))
        await query.edit_message_text("✅ Pago confirmado y usuario notificado.")

# ========================
# Función principal
# ========================
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={SELECT_LANG: [CallbackQueryHandler(select_language)]},
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot multilenguaje ejecutándose...")
    app.run_polling()

# ========================
# EJECUCIÓN
# ========================
if __name__ == "__main__":
    main()
