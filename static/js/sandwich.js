var theater = theaterJS()
  
theater
  .on('type:start, erase:start', function () {
    // add a class to actor's dom element when he starts typing/erasing
    var actor = theater.getCurrentActor()
    actor.$element.classList.add('is-typing')
  })
  .on('type:end, erase:end', function () {
    // and then remove it when he's done
    var actor = theater.getCurrentActor()
    actor.$element.classList.remove('is-typing')
  })

theater
  .addActor('jjbot')
  
theater
  .addScene('jjbot:This is a test to see what happens.', 400)
  .addScene(theater.replay)