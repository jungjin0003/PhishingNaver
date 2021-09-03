function Close_Nudge_Banner() {
    document.getElementById('nudge_tooltip').style.display = "none";
}

function Change_Menu(index) {
    tabs = document.getElementsByClassName('menu_item');
    for (i = 0; i < 3; i++) {
        tabs[i].setAttribute('aria-selected', false);
        tabs[i].getElementsByTagName('a')[0].setAttribute('class', tabs[i].getElementsByTagName('a')[0].getAttribute('class').split(' ')[0]);
    }
    tab = tabs[index];
    tab.setAttribute('aria-selected', true);
    tab = tab.getElementsByTagName('a')[0];
    tab.setAttribute('class', tab.getAttribute('class') + ' on');
    switch (index) {
        case 0:
            loinid_string = `                    <input type="hidden" id="mode" name="mode" value="form">
                    <ul class="panel_wrap">
                        <li class="panel_item" style="display: block;">
                            <div class="panel_inner" role="tabpanel" aria-controls="loinid">
                                <div class="id_pw_wrap">
                                    <div class="input_row" id="id_line">
                                        <div class="icon_cell" id="id_cell">
                                            <span class="icon_id">
                                                <span class="blind">아이디</span>
                                            </span>
                                        </div>
                                        <input type="text" id="id" name="id" placeholder="아이디" title="아이디" class="input_text" maxlength="41" value="">
                                        <span role="button" class="btn_delete" id="id_clear" style="display: none;">
                                            <span class="icon_delete">
												<span class="blind">삭제</span>
                                            </span>
                                        </span>
                                    </div>
                                    <div class="input_row" id="pw_line">
                                        <div class="icon_cell" id="pw_cell">
                                            <span class="icon_pw">
                                                <span class="blind">비밀번호</span>
                                            </span>
                                        </div>
                                        <input type="password" id="pw" name="pw" placeholder="비밀번호" title="비밀번호" class="input_text" maxlength="16">
                                        <span role="button" class="btn_delete" id="pw_clear" style="display: none;">
                                            <span class="icon_delete">
                                                <span class="blind">삭제</span>
                                            </span>
                                        </span>
                                    </div>
                                </div>
                                <div class="login_keep_wrap" id="login_keep_wrap">
                                    <div class="keep_check">
                                        <input type="checkbox" id="keep" name="nvlong" class="input_keep" value="off">
                                        <label for="keep" class="keep_text">로그인 상태 유지</label>
                                    </div>
                                    <div class="ip_check">
                                        <a href="/login/ext/help_ip3.html" target="_blank" id="ipguide" title="IP보안"><span class="ip_text">IP보안</span></a>
                                        <span class="switch">
                                            <input type="checkbox" id="switch" class="switch_checkbox" value="off">
                                            <label for="switch" class="switch_btn">
                                                <span class="blind" id="switch_blind">on</span>
                                            </label>
                                        </span>
                                    </div>
                                </div>

                                <div class="login_error_wrap" id="err_capslock" style="display: none;">
                                    <div class="error_message">
                                        <strong>CapsLock</strong>이 켜져 있습니다.
                                    </div>
                                </div>

                                <div class="login_error_wrap" id="err_empty_id" style="display: none;">
                                    <div class="error_message">
                                        <strong>아이디</strong>를 입력해 주세요.
                                    </div>
                                </div>

                                <div class="login_error_wrap" id="err_empty_pw" style="display: none;">
                                    <div class="error_message">
                                        <strong>비밀번호</strong>를 입력해 주세요.
                                    </div>
                                </div>
                                <div class="login_error_wrap" id="err_common" style="display:none;">
                                    <div class="error_message" style="width:90%">
                                        
                                    </div>
                                </div>
                                <div class="btn_login_wrap">

                                    <button type="submit" class="btn_login" id="log.login">
                                        <span class="btn_text">로그인</span>
                                    </button>

                                </div>
                            </div>
                        </li>
                    </ul>`
            window.frmNIDLogin.innerHTML = loinid_string;
            break;

        case 1:
            ones_string = `                    <input type="hidden" id="mode" name="mode" value="ones">
                    <ul class="panel_wrap">
                        <li class="panel_item" style="display: block;">

                            <div class="panel_inner" role="tabpanel" aria-controls="ones">
                                <!--안내-->
                                <div class="img_lock" aria-hidden="true"></div>
                                <div class="ones_text">
                                    네이버앱의 <span class="accent">메뉴 &gt; 설정 <em class="bullet_set"></em> &gt; 로그인 아이디 관리<br> &gt; 일회용 로그인 번호 받기</span>에
                                    보이는 번호를 입력해 주세요.
                                </div>

                                <!--일회용입력창-->
                                <div class="input_row" id="num_line">
                                    <input type="text" id="disposable" name="key" placeholder="일회용 로그인 번호" title="일회용 로그인 번호" class="input_text">
                                    <span role="button" class="btn_delete" id="num_clear" style="display: none;">
                                        <span class="icon_delete"><span class="blind">삭제</span></span>
                                    </span>
                                </div>
                                <div class="login_error_wrap" id="err_empty_no" style="display:none;margin-top:0px;">
                                    <span class="error_message">일회용 로그인 번호를 입력하세요.</span>
                                </div>
                                <div class="login_error_wrap" id="err_empty_no2" style="display:none;margin-top:0px;">
                                    <span class="error_message">일회용 로그인 번호를 다시 입력해 주세요.<br>일회용 로그인 번호를 확인한 후 8자리 숫자를 다시 입력해 주세요.</span>
                                </div>
                                <div class="login_error_wrap" id="err_common" style="display:none;margin-top:0px;">
                                    <span class="error_message">
                                        <div class="error">일회용 로그인 번호를 확인한 후 다시 입력해 주세요.</div>
                                    </span>
                                </div>
                                <!--버튼-->
                                <div class="btn_ones_wrap">

                                    <button type="submit" class="btn_login" id="otnlog.login">
                                        <!-- tg-text=loginbtn -->
                                        <span class="btn_text">로그인</span>
                                    </button>

                                </div>
                            </div>

                        </li>
                    </ul>`;
            window.frmNIDLogin.innerHTML = ones_string;
            break;

        case 2:
            qrcode_string = `                    <input type="hidden" id="mode" name="mode" value="qrcode">
                    <ul class="panel_wrap">
                        <li class="panel_item" style="display: block;">

                            <!-- tg-display=>{"QR코드": []} -->
                            <div class="panel_inner" role="tabpanel" aria-controls="qrcode" id="qrImageDiv" style="display: none;">
                                <h2 class="top_desc">공용 네트워크, 공용 PC라면 안전을 위해<br> QR코드로 로그인해주세요.</h2>
                                <div class="sub_desc">
                                    <span class="text">네이버 앱 <em class="bullet_greendot"></em> &gt; 렌즈 <em class="bullet_lens"></em> 를 눌러 QR코드를 스캔하여<br> 보이는 숫자 중 <strong class="point"></strong>를 선택하면 로그인 됩니다.</span>
                                    <a href="#none" id="qrbanner_open" class="bullet_help"><span class="blind">도움말</span></a>
                                </div>
                                <div class="qrcode_map">
                                    <img src="" width="174" height="174" alt="QR Code" id="qrImage" class="qr_img" style="padding:0px;">
                                </div>
                                <div class="time_wrap">
                                    <p class="time_text">남은시간</p>
                                    <p class="time_num" id="timeStamp">00:00</p>
                                </div>
                            </div>
                            <div class="panel_inner" role="tabpanel" aria-controls="qrcode" id="reloadGuide" style="display: none;">
                                <div class="qrcode_valid">
                                    <p class="img_wowpoint"></p>
                                    <h2 class="top_desc">QR코드 유효시간 초과</h2>
                                    <div class="sub_desc">
                                        해당 QR코드의 유효시간이 지났습니다.<br> 다시 로그인을 시도하시겠습니까?
                                    </div>
                                    <div class="time_wrap">
                                        <a href="#" id="qrlog.retry" class="btn_renewal">재시도</a>
                                    </div>
                                </div>
                            </div>
                            <!-- tg-display -->
                        </li>
                    </ul>`
            window.frmNIDLogin.innerHTML = qrcode_string;
            break;
        default:
            break;
    }
}