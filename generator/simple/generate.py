import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='run1')
gpt2.generate(
    sess,
    run_name='run1',
    length=250,
    temperature=0.7,
    prefix="Lord",
    nsamples=5,
    batch_size=5
)
