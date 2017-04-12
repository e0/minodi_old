function build-stack {
    docker-compose -p minodi build $@
}

function start-stack {
    docker-compose -p minodi up -d
}

function stop-stack {
    docker-compose -p minodi kill
}


function restart-stack {
    stop-stack && start-stack
}

function logs {
    docker-compose -p minodi logs -f $@
}

function build-production {
    docker exec minodi_site_1 npm run build
    rm -rf nginx/static
    mkdir nginx/static
    cp -r site/dist/ nginx/
    mv nginx/index.html nginx/static/
}

echo -e "
Available commands:
\tbuild-stack
\tstart-stack
\tstop-stack
\trestart-stack
\tlogs
\tbuild-production
"
