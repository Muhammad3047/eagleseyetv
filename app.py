import http.server
import socketserver
import webbrowser
import threading
import time

# ==============================================================================
# EAGLE'S EYE TV — NEXT-GEN PREMIUM ARCHITECTURE CORE
# Fully compliant with feature documents: 8a50b27a and 1508b925
# ==============================================================================

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EAGLE'S EYE TV | Next-Gen Unified Command Matrix</title>
    <style>
        :root {
            --bg-deep: #030611;
            --bg-surface: #0a0f24;
            --bg-input: #121938;
            --primary: #ff2a5f;       /* Premium Crimson Accent */
            --accent: #ffcc00;        /* Luxury Sovereign Gold */
            --text-pure: #ffffff;
            --text-dim: #94a3b8;
            --verified: #00f0ff;
            --admin-glow: #ff3333;
            --success: #10b981;
            --glass-border: rgba(255, 255, 255, 0.07);
        }

        body {
            background-color: var(--bg-deep);
            color: var(--text-pure);
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        /* --- AUTHENTICATION INTERCEPT protocol GATEWAY OVERLAY --- */
        .gateway-container {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, #010308 0%, #050917 100%);
            z-index: 9999;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .gateway-card {
            background: var(--bg-surface);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            width: 100%;
            max-width: 420px;
            padding: 30px;
            box-shadow: 0 25px 60px rgba(0,0,0,0.8);
            text-align: center;
        }

        .auth-nav {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin-bottom: 25px;
            border-bottom: 1px solid rgba(255,255,255,0.08);
            padding-bottom: 12px;
        }

        .auth-btn {
            background: none;
            border: none;
            color: var(--text-dim);
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            transition: color 0.3s;
        }

        .auth-btn.active {
            color: var(--accent);
            border-bottom: 2px solid var(--accent);
        }

        /* --- FIXED BRAND HEADER BAR --- */
        .header-bar {
            background: rgba(3, 6, 17, 0.96);
            backdrop-filter: blur(20px);
            position: sticky;
            top: 0;
            z-index: 1000;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--glass-border);
        }

        .brand-wrapper {
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
        }

        .brand-icon {
            width: 36px;
            height: 36px;
            background: linear-gradient(135deg, #ffcc00 0%, #ff5500 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            box-shadow: 0 0 15px rgba(255,204,0,0.2);
        }

        .brand-name {
            font-size: 18px;
            font-weight: 900;
            letter-spacing: 0.5px;
            background: linear-gradient(90deg, #ffffff 0%, var(--accent) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* --- MAIN VIEWPORT FRAME --- */
        .app-viewport {
            max-width: 480px;
            margin: 0 auto;
            padding: 15px;
            padding-bottom: 100px;
        }

        .view-panel {
            display: none;
        }

        .view-panel.active {
            display: block;
        }

        /* --- GLOBAL INPUT ARTIFACT ARCHITECTURES --- */
        input, textarea, select {
            width: 100%;
            padding: 14px 18px;
            margin-top: 10px;
            background: var(--bg-input);
            border: 1px solid var(--glass-border);
            color: white;
            border-radius: 14px;
            box-sizing: border-box;
            font-size: 14px;
            transition: all 0.3s;
        }
        input:focus, textarea:focus {
            border-color: var(--accent);
            box-shadow: 0 0 12px rgba(255,204,0,0.15);
            outline: none;
        }

        .action-submit-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(90deg, var(--primary) 0%, #ff557f 100%);
            color: white;
            border: none;
            border-radius: 14px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 15px;
            box-shadow: 0 6px 20px rgba(255,42,95,0.25);
            transition: transform 0.2s, opacity 0.2s;
        }
        .action-submit-btn:active { transform: scale(0.98); opacity: 0.95; }

        .toggle-row-setting {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 12px;
            background: var(--bg-input);
            padding: 14px;
            border-radius: 14px;
            border: 1px solid var(--glass-border);
        }
        .toggle-row-setting span { font-size: 13.5px; font-weight: 600; }
        .toggle-row-setting input[type="checkbox"] { width: auto; margin: 0; cursor: pointer; }

        /* --- LIVE BROADCAST TIKTOK HORIZONTAL SCROLL CORE --- */
        .live-tray-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }
        .live-tray-header h5 { margin: 0; font-size: 11px; text-transform: uppercase; color: var(--text-dim); letter-spacing: 1px; }

        .live-stream-scroll {
            display: flex;
            gap: 14px;
            overflow-x: auto;
            padding-bottom: 12px;
            margin-bottom: 20px;
        }
        .live-stream-scroll::-webkit-scrollbar { display: none; }

        .live-avatar-frame {
            position: relative;
            min-width: 68px;
            max-width: 68px;
            text-align: center;
            cursor: pointer;
        }
        .live-circle {
            width: 58px;
            height: 58px;
            border-radius: 50%;
            background: #111528;
            border: 2.5px solid var(--primary);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin: 0 auto;
            overflow: hidden;
        }
        .live-circle img { width: 100%; height: 100%; object-fit: cover; }
        .live-badge {
            position: absolute;
            bottom: 14px;
            left: 50%;
            transform: translateX(-50%);
            background: var(--primary);
            color: white;
            font-size: 8px;
            font-weight: 900;
            padding: 2px 6px;
            border-radius: 8px;
            text-transform: uppercase;
        }
        .live-name {
            font-size: 11px;
            color: var(--text-dim);
            margin-top: 5px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* --- IMMERSIVE LIVE INTERACTIVE STREAMING STAGE OVERLAY --- */
        .live-stage-overlay {
            background: #02040a;
            border-radius: 24px;
            border: 2px solid var(--primary);
            margin-bottom: 25px;
            padding: 16px;
            display: none;
            box-shadow: 0 0 30px rgba(255,42,95,0.2);
        }
        .live-stage-screen {
            background: linear-gradient(180deg, #050a1e 0%, #010205 100%);
            height: 220px;
            border-radius: 16px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(255,255,255,0.05);
        }
        .live-stage-metrics {
            position: absolute;
            top: 12px; left: 12px; right: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: calc(100% - 24px);
        }
        .live-stage-comments-ticker {
            width: 100%;
            height: 75px;
            overflow-y: auto;
            margin-top: 12px;
            background: rgba(255,255,255,0.02);
            border-radius: 10px;
            padding: 8px;
            box-sizing: border-box;
            font-size: 12px;
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        /* --- SYSTEM GLOBAL RECOVERY/BROADCAST ALERTS --- */
        .system-broadcast-banner {
            background: linear-gradient(90deg, #79112c 0%, var(--primary) 100%);
            border: 1px solid var(--primary);
            padding: 14px;
            border-radius: 16px;
            margin-bottom: 20px;
            font-size: 13px;
            font-weight: 700;
            line-height: 1.4;
            display: none;
            position: relative;
        }

        /* --- PREMIUM TIED SOCIAL CARDS --- */
        .luxury-post-card {
            background: var(--bg-surface);
            border-radius: 24px;
            border: 1px solid var(--glass-border);
            margin-bottom: 25px;
            overflow: hidden;
            box-shadow: 0 12px 40px rgba(0,0,0,0.5);
        }

        .post-media-frame {
            width: 100%;
            min-height: 240px;
            background: #010307;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
        }
        .post-media-frame img, .post-media-frame video {
            width: 100%; height: auto; max-height: 440px; object-fit: contain;
        }

        .download-pill-indicator {
            position: absolute;
            top: 14px; right: 14px;
            background: rgba(0,0,0,0.65);
            backdrop-filter: blur(10px);
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: bold;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .post-details-box { padding: 18px; }
        .post-profile-row { display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px; }
        
        .author-meta-block { display: flex; align-items: center; gap: 10px; cursor: pointer; }
        .author-avatar { width: 36px; height: 36px; border-radius: 50%; background: var(--bg-input); border: 1px solid var(--accent); display:flex; align-items:center; justify-content:center; font-size:16px; overflow:hidden;}
        .author-avatar img { width:100%; height:100%; object-fit:cover; }
        .author-handle { font-weight: 800; font-size: 14px; color: var(--text-pure); }
        .author-handle span { font-size: 11px; color: var(--text-dim); display: block; font-weight: 400; }

        .post-caption-text { font-size: 14px; color: #cbd5e1; line-height: 1.5; margin: 8px 0; }
        
        .post-view-counter-strip { font-size: 11px; color: var(--text-dim); font-weight: 700; margin-bottom: 5px; text-transform: uppercase; letter-spacing: 0.5px;}

        /* --- AUTHENTIC INTERACTION HUD TOOLBAR --- */
        .post-actions-toolbar {
            display: flex;
            justify-content: space-around;
            padding: 12px;
            border-top: 1px solid rgba(255,255,255,0.03);
            background: rgba(0,0,0,0.15);
        }
        .toolbar-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            color: var(--text-dim);
        }
        .toolbar-item.active-liked { color: var(--primary); }

        .comments-expansion-tray {
            background: rgba(0,0,0,0.25);
            border-top: 1px solid rgba(255,255,255,0.03);
            padding: 15px;
            display: none;
        }
        .comments-list-stream {
            max-height: 150px;
            overflow-y: auto;
            margin-bottom: 12px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .comment-node { font-size: 12.5px; line-height: 1.4; color: #e2e8f0; }
        .comment-node b { color: var(--accent); margin-right: 5px; }

        /* --- LOCAL ENCRYPTED DIRECT MESSAGING WINDOWS --- */
        .chat-container-window {
            background: var(--bg-surface);
            border-radius: 20px;
            border: 1px solid var(--glass-border);
            padding: 16px;
            margin-top: 15px;
        }
        .chat-logs-box {
            height: 180px;
            overflow-y: auto;
            background: #02040a;
            border-radius: 12px;
            padding: 12px;
            margin-bottom: 12px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            border: 1px solid rgba(255,255,255,0.04);
        }
        .chat-bubble { padding: 10px 14px; border-radius: 14px; max-width: 80%; font-size: 13px; line-height: 1.4; }
        .chat-bubble.sent { background: var(--primary); align-self: flex-end; color: white; border-bottom-right-radius: 2px; }
        .chat-bubble.received { background: var(--bg-input); align-self: flex-start; color: white; border-bottom-left-radius: 2px; }

        /* --- FIXED BOTTOM NAVIGATION BAR --- */
        .bottom-hud-nav {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background: rgba(3, 6, 17, 0.97);
            border-top: 1px solid var(--glass-border);
            display: flex;
            justify-content: space-around;
            padding: 12px 0;
            z-index: 2000;
        }
        .hud-item {
            background: none; border: none; color: var(--text-dim);
            font-size: 11px; font-weight: 700; cursor: pointer;
            display: flex; flex-direction: column; align-items: center; gap: 5px;
        }
        .hud-item.active { color: var(--accent); }
        .center-post-trigger {
            background: linear-gradient(135deg, var(--accent) 0%, #ffaa00 100%);
            width: 44px; height: 44px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            color: #000 !important; font-weight: 900; font-size: 24px;
            box-shadow: 0 0 15px rgba(255,204,0,0.35);
            margin-top: -12px;
        }

        .toast-popup {
            position: fixed;
            top: 75px; left: 5%; right: 5%;
            background: var(--accent); color: #000;
            padding: 12px; border-radius: 12px;
            text-align: center; font-weight: 800; font-size: 13px;
            display: none; z-index: 5000;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }
        
        .invite-modal-backdrop {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.8); z-index: 6000;
            display: none; align-items: center; justify-content: center; padding: 20px;
        }
    </style>
</head>
<body>

<div id="identityGateway" class="gateway-container">
    <div class="gateway-card">
        <div class="auth-nav">
            <button id="tabBtnSignIn" class="auth-btn active" onclick="toggleAuthGatewayTab('signin')">Sign In</button>
            <button id="tabBtnSignUp" class="auth-btn" onclick="toggleAuthGatewayTab('signup')">Sign Up</button>
            <button id="tabBtnRecover" class="auth-btn" onclick="toggleAuthGatewayTab('recover')">Recover</button>
        </div>
        
        <h3 id="gatewayTitle" style="margin-top:0; color:#fff;">Welcome back to Eagle's Eye TV</h3>
        
        <div id="signUpFieldsArea" style="display:none;">
            <input type="text" id="regFullName" placeholder="Enter Full Name">
            <input type="text" id="regEmail" placeholder="Enter Email Address">
            <select id="regAvatarSelection">
                <option value="🦅">🦅 Crown Eagle Avatar</option>
                <option value="👑">👑 Gold Royalty Crown</option>
                <option value="💻">💻 Tech Master Terminal</option>
                <option value="🎂">🎂 Premium Baker Elite</option>
                <option value="🔥">🔥 Creative Catalyst</option>
            </select>
        </div>

        <div id="recoveryFieldsArea" style="display:none;">
            <input type="text" id="recoveryEmailInput" placeholder="Enter Registered Email Address">
            <div id="verificationCodeFieldBox" style="display:none; background:rgba(255,255,255,0.02); padding:12px; border-radius:12px; margin-top:10px;">
                <p style="font-size:11px; color:var(--accent); margin:0 0 8px 0;">Verification code sent! Enter code below:</p>
                <input type="text" id="recoveryCodeVerificationInput" placeholder="6-Digit Verification Token">
            </div>
        </div>

        <div id="primaryAuthInputGroup">
            <input type="text" id="regUsername" placeholder="Username Handle (e.g. @Ibrahim_isah)">
            <input type="password" id="regPassword" placeholder="Security Password">
        </div>
        
        <button id="gatewaySubmitActionButton" class="action-submit-btn" onclick="executeGatewayAuthorization()">Enter Portal Network</button>
    </div>
</div>

<div class="header-bar">
    <div class="brand-wrapper" onclick="navigateToPanel('feed')">
        <div class="brand-icon">🦅</div>
        <div class="brand-name">EAGLE'S EYE TV</div>
    </div>
    <div id="adminBadgeIndicator" style="display:none; font-size:10px; background:var(--admin-glow); color:white; padding:5px 12px; border-radius:20px; font-weight:800; letter-spacing:0.5px;">MASTER OVERRIDE ADMIN</div>
</div>

<div class="app-viewport">
    <div id="toastNotification" class="toast-popup"></div>

    <div id="globalSystemBroadcastBanner" class="system-broadcast-banner">
        <span style="color:var(--accent); font-weight:900; display:block; text-transform:uppercase; font-size:11px; margin-bottom:4px;">📢 NETWORK BROADCAST ANNOUNCEMENT:</span>
        <span id="globalBroadcastBannerMessageBody">Welcome to the premium architecture network framework stream.</span>
        <span style="position:absolute; top:8px; right:12px; cursor:pointer; font-size:12px; opacity:0.7;" onclick="this.parentElement.style.display='none'">✕</span>
    </div>

    <div id="panel-feed" class="view-panel active">
        
        <div style="display:flex; gap:10px; margin-bottom:15px;">
            <input type="text" id="feedSearchBox" style="margin:0;" placeholder="🔍 Search username, content or full name..." oninput="filterTimelineContent()">
            <button class="action-submit-btn" style="width:auto; margin:0; padding:0 15px; background:var(--bg-surface); border:1px solid var(--glass-border);" onclick="triggerInviteModalLaunch()">✉ Invite</button>
        </div>

        <div class="live-tray-header">
            <h5>Core Live Broadcasters</h5>
            <span style="font-size:10px; color:var(--primary); font-weight:bold; animation: pulse 1s infinite;">● REALTIM