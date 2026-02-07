(() => {
  const updateActiveState = (choice) => {
    if (!choice) {
      return;
    }

    const wizard = choice.closest('.cms-content-wizard');
    if (!wizard) {
      return;
    }

    wizard.querySelectorAll('.choice').forEach((item) => {
      item.classList.toggle('active', item === choice);
    });
  };

  const ensureWizardSelection = (event) => {
    const choice = event.target.closest('.cms-content-wizard .choice');
    if (!choice) {
      return;
    }

    if (['keydown', 'keyup'].includes(event.type) && !['Enter', ' '].includes(event.key)) {
      return;
    }

    const input = choice.querySelector('input[type="radio"]');
    if (!input) {
      return;
    }

    input.checked = true;
    input.dispatchEvent(new Event('input', { bubbles: true }));
    input.dispatchEvent(new Event('change', { bubbles: true }));
    if (event.type === 'click') {
      input.dispatchEvent(new Event('click', { bubbles: true }));
    }
    updateActiveState(choice);
  };

  const selectDefaultChoice = () => {
    document.querySelectorAll('.cms-content-wizard').forEach((wizard) => {
      const checked = wizard.querySelector('.choice input[type="radio"]:checked');
      if (checked) {
        updateActiveState(checked.closest('.choice'));
        return;
      }

      const firstChoice = wizard.querySelector('.choice');
      if (!firstChoice) {
        return;
      }

      const input = firstChoice.querySelector('input[type="radio"]');
      if (!input) {
        return;
      }

      input.checked = true;
      input.dispatchEvent(new Event('input', { bubbles: true }));
      input.dispatchEvent(new Event('change', { bubbles: true }));
      updateActiveState(firstChoice);
    });
  };

  document.addEventListener('click', ensureWizardSelection);
  document.addEventListener('keydown', ensureWizardSelection);
  document.addEventListener('keyup', ensureWizardSelection);
  document.addEventListener('DOMContentLoaded', selectDefaultChoice);
  window.addEventListener('load', selectDefaultChoice);
})();
