package com.internship.tool.service;

import com.internship.tool.entity.Compliance;
import com.internship.tool.repository.ComplianceRepository;
import com.internship.tool.exception.ResourceNotFoundException;

import org.springframework.stereotype.Service;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import java.util.List;

@Service
public class ComplianceService {

    private final ComplianceRepository repository;

    public ComplianceService(ComplianceRepository repository) {
        this.repository = repository;
    }

    
    public Compliance createCompliance(Compliance compliance) {
        return repository.save(compliance);
    }

    
    public List<Compliance> getAllCompliance() {
        return repository.findAll();
    }

    
    public Page<Compliance> getAllPaginated(Pageable pageable) {
        return repository.findAll(pageable);
    }

   
    public Compliance getComplianceById(Long id) {
        return repository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException(
                        "Compliance not found with id: " + id));
    }

    
    public Compliance updateCompliance(Long id, Compliance updated) {
        Compliance existing = getComplianceById(id);

        existing.setTitle(updated.getTitle());
        existing.setDescription(updated.getDescription());
        existing.setCategory(updated.getCategory());
        existing.setStatus(updated.getStatus());
        existing.setDueDate(updated.getDueDate());
        existing.setRiskScore(updated.getRiskScore());

        return repository.save(existing);
    }

    // ✅ DELETE
    public void deleteCompliance(Long id) {
        if (!repository.existsById(id)) {
            throw new ResourceNotFoundException(
                    "Compliance not found with id: " + id);
        }
        repository.deleteById(id);
    }
}