<!--        {% if current_user.is_authenticated %}-->
<!--            {{ current_user.username }}-->
<!--        {% else %}-->
<!--            anon-->
<!--        {% endif %}-->

<!--              <div class="navbar-nav ms-auto">-->
<!--                  {% if current_user.is_authenticated %}-->
<!--                    <a class="nav-link" href="{{ url_for('logout') }}">Logout</a>-->
<!--                  {% else %}-->
<!--                      <a href="{{ url_for('login') }}"-->
<!--                         class="nav-link {% if request.endpoint == 'login' -%}active{%- endif %}">-->
<!--                          Login-->
<!--                      </a>-->
<!--                  {% endif %}-->
<!--              </div>-->
