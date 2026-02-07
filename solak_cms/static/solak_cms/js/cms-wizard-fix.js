(() => {
  const ensureWizardSelection = (event) => {
    const choice = event.target.closest('.cms-content-wizard .choice');
    if (!choice) {
      return;
    }

    if (event.type === 'keyup' && !['Enter', ' '].includes(event.key)) {
      return;
    }

    const input = choice.querySelector('input[type="radio"]');
    if (!input) {
      return;
    }

    input.checked = true;
    input.dispatchEvent(new Event('change', { bubbles: true }));
  };

  document.addEventListener('click', ensureWizardSelection);
  document.addEventListener('keyup', ensureWizardSelection);
})();
