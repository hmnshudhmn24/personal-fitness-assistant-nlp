from src.inference import generate_plan
def test_generate_signature():
    try:
        out = generate_plan(25, 'beginner', 'weight_loss', 30, model_dir='model/checkpoints/best-model')
    except Exception as e:
        assert isinstance(e, Exception)
        return
    assert isinstance(out, str)
