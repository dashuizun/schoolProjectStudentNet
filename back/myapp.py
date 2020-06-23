from app import create_app

# 配置app
app = create_app('default')

# 屏蔽JINJA2 防止和VUE冲突
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'

if __name__ == '__main__':
    app.run()
