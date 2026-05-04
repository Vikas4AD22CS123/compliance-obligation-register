package com.internship.tool.service;

import com.internship.tool.entity.Compliance;
import com.internship.tool.repository.ComplianceRepository;
import com.internship.tool.exception.ResourceNotFoundException;

import org.springframework.stereotype.Service;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

import org.springframework.cache.annotation.Cacheable;
import org.springframework.cache.annotation.CacheEvict;

import java.util.List;

@Service
public class ComplianceService {

    private final ComplianceRepository repository;
    private final EmailService emailService;

    // ✅ Constructor
    public ComplianceService(ComplianceRepository repository,
                             EmailService emailService) {
        this.repository = repository;
        this.emailService = emailService;
    }

    // ✅ CREATE (Clear cache + Send Email)
    @CacheEvict(value = "compliance", allEntries = true)
    public Compliance createCompliance(Compliance compliance) {

        Compliance saved = repository.save(compliance);

        // 📧 Send Email
        emailService.sendComplianceEmail(
                "your_email@gmail.com", // ⚠️ change this
                saved.getTitle(),
                "New compliance created: " + saved.getDescription()
        );

        return saved;
    }

    // ✅ GET ALL
    public List<Compliance> getAllCompliance() {
        return repository.findAll();
    }

    // ✅ GET PAGINATED (Cached)
    @Cacheable(value = "compliance", key = "'page_'+#pageable.pageNumber")
    public Page<Compliance> getAllPaginated(Pageable pageable) {
        return repository.findAll(pageable);
    }

    // ✅ GET BY ID (Cached)
    @Cacheable(value = "compliance", key = "#id")
    public Compliance getComplianceById(Long id) {
        return repository.findById(id)
                .orElseThrow(() ->
                        new ResourceNotFoundException(
                                "Compliance not found with id: " + id));
    }

    // ✅ UPDATE (Clear cache)
    @CacheEvict(value = "compliance", allEntries = true)
    public Compliance updateCompliance(Long id, Compliance updated) {

        Compliance existing = getComplianceById(id);

        existing.setTitle(updated.getTitle());
        existing.setDescription(updated.getDescription());
        existing.setCategory(updated.getCategory());
        existing.setStatus(updated.getStatus());
        existing.setDueDate(updated.getDueDate());
        existing.setRiskScore(updated.getRiskScore());

        Compliance saved = repository.save(existing);

        // 📧 Optional: Send update email
        emailService.sendComplianceEmail(
                "your_email@gmail.com",
                saved.getTitle(),
                "Compliance updated"
        );

        return saved;
    }

    // ✅ DELETE (Clear cache)
    @CacheEvict(value = "compliance", allEntries = true)
    public void deleteCompliance(Long id) {

        if (!repository.existsById(id)) {
            throw new ResourceNotFoundException(
                    "Compliance not found with id: " + id);
        }

        repository.deleteById(id);
    }
}